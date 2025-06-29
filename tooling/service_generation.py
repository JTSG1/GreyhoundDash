from openai import OpenAI
import json
import re
from pydantic import BaseModel
from github import Github
import os
import subprocess
from hashlib import md5
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GithubPRCreator:
    """
    This class is responsible for creating a pull request in the GitHub repository.
    It uses the GitHub API to create the pull request.
    """
    def __init__(self, github_client: Github, repo_name: str, base_branch: str = "main"):

        self.github_client = github_client
        self.repo = self.github_client.get_repo(repo_name)
        self.base = self.repo.get_branch(base_branch)

    def create_branch_and_raise_pr(self, branch_name: str, *, add_all: bool = True, services: list = None):
        """
        Create a new branch in the GitHub repository.
        """

        logging.info(f"Creating branch '{branch_name}' and raising a PR.")

        try:
            self.repo.get_branch(branch_name)
            raise ValueError(f"Remote branch '{branch_name}' already exists")
        except Exception:
            pass  # branch really does not exist

        # 1. create & switch
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)

        # 2. stage changes
        if add_all:
            subprocess.run(["git", "add", "-A"], check=True)

        # 3. commit (will throw if nothing staged)
        subprocess.run(
            ["git", "commit", "-m", "feat: automated bot commit for services"],
            check=True,
        )

        # 4. push and set upstream (creates remote ref)
        subprocess.run(["git", "push", "-u", "origin", branch_name], check=True)

        # 5. switch back
        subprocess.run(["git", "checkout", "main"], check=True)

        pr = self.repo.create_pull(                         
            title = f"Add new basic services from service generation {services[0]} to {services[-1]}",
            body = "This implements the following services:\n\n" + "\n".join(f"{name}: {created}" for name, created in services),
            head  = branch_name,         # what you just created
            base  = "main",             # where you want it merged
            draft = False               # or True for a draft PR
        )

        logging.info(f"Pull request created: {pr.html_url}")


class ServiceGenerator:
    """
    This class is responsible for generating service code based on a template and provided parameters.
    It uses the OpenAI API to generate the code and save it to a file.
    """
    COMPLETED_SERVICE_PATH = "tooling/awesome_selfhosted_services_completed.json"
    PR_FREQUENCY = 10  # Number of services to process before creating a PR
    BATCH_SIZE = 10  # Number of services to process in one run
    GPT_MODEL = "gpt-4o-mini"  # Model to use for OpenAI API

    def __init__(self, prompt_template_path: str = "tooling/service_generation_prompt.txt", openai_client: OpenAI = None, github_pr_creator: GithubPRCreator = None):
        self.openai_client = openai_client
        self.prompt_template = open(prompt_template_path, "r").read()
        self.service_data = self.__parse_retrieved_service_data()
        self.completed_services = self.__get_completed_list()

        self.github_pr_creator = github_pr_creator

        if self.BATCH_SIZE % self.PR_FREQUENCY != 0:
            raise ValueError("BATCH_SIZE must be a multiple of PR_FREQUENCY to ensure even distribution of services in PRs.")

    def replace_template_variables(
        self,
        template: str, 
        base_class_file: str, 
        base_class_name: str,
        implementation_samples: str,
        json_schema: dict,
        service_name: str, 
        service_homepage: str) -> str: 

        logging.debug("Replacing template variables in the prompt template.")
    
        template = template.replace("{% base_class_file %}", base_class_file)
        template = template.replace("{% base_class_name %}", base_class_name)
        template = template.replace("{% implementation_samples %}", implementation_samples)
        template = template.replace("{% service_name %}", service_name)
        template = template.replace("{% service_homepage %}", service_homepage)
        template = template.replace("{% json_schema %}", str(json_schema))

        return template

    def generate_service_code(self, service_name: str, homepage: str, call_count = 0) -> str:

        logging.info(f"Generating code for service: {service_name} (attempt {call_count + 1})")

        prompt = self.replace_template_variables(
            self.prompt_template,
            base_class_file=open("greyhoundDashboard/services/service_base.py", "r").read(),
            base_class_name="ServiceBase",
            implementation_samples=open("greyhoundDashboard/services/basic_services/service_grafana.py", "r").read(),
            json_schema=json.dumps(JSON_RESPONSE_SCHEMA, indent=2),
            service_name=service_name,
            service_homepage=homepage
        )
        try:

            response = self.openai_client.responses.parse(
                model=self.GPT_MODEL,
                input=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that generates code for services."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                text_format=ServiceResponseSchema,
                tool_choice="required",
                tools=[{"type": "web_search_preview"}],
                temperature=0.1
            )
            
            content = response.output_parsed
        except Exception as e:
            logging.error(f"Error parsing response for service {service_name}: {e}")
            if call_count < 5:
                logging.info(f"Retrying for service {service_name} (attempt {call_count + 1})...")
                return self.generate_service_code(service_name, homepage, call_count + 1)
            else:
                logging.error(f"Failed to generate code for service {service_name} after 5 attempts.")
                return False

        if content.web_app:

            # Save the generated code to a file
            with open(f"greyhoundDashboard/services/basic_services/{content.file_name}", "w") as code_file:
                code_file.write(content.code)

            # Save the logo to a file
            logo_url = content.logo
            # ignoring images for now
            return True
        else:
            logging.warning(f"Service {service_name} is not a web app. Skipping code generation.")
            return False
        
    def __parse_retrieved_service_data(self):

        logging.info("Parsing retrieved service data from JSON file.")

        with open("tooling/awesome_selfhosted_services.json", "r") as file:
            data = json.load(file)

        return data
    
    def __get_completed_list(self):

        logging.info("Loading completed services from JSON file.")

        try:
            with open(self.COMPLETED_SERVICE_PATH, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    logging.error(f"Error decoding JSON from {self.COMPLETED_SERVICE_PATH}. Returning an empty list.")
                    data = {}
        except FileNotFoundError:
            logging.error(f"Completed services file not found at {self.COMPLETED_SERVICE_PATH}. Returning an empty list.")
            data = {}

        return data

    def iterate_services(self):
        """
        Iterate through the service data and generate code for each service.
        """
        
        logging.info("Starting to iterate through services to generate code.")

        counter = 0

        local_added = []

        for service_name, service_info in self.service_data.items():

            logging.info(f"Processing service: {service_name}")

            if self.completed_services.get(service_name):
                logging.info(f"Service {service_name} already processed.")
                continue
            
            logging.info(f"Generating code for {service_name}...")
            created = self.generate_service_code(service_name, service_info['homepage'])
            self.complete_service(
                service_name = service_info['name'],
                service_info = service_info,
                created = created
            )

            local_added.append((service_info['name'], created))

            counter += 1

            if counter % self.PR_FREQUENCY == 0:

                logging.info("Processed 10 services. Stopping for now to avoid rate limits. Creating a branch and raising a PR...")

                self.github_pr_creator.create_branch_and_raise_pr(
                    branch_name=f"feat/service-generation-{counter}-{md5(''.join(f"{name}: {created}" for name, created in local_added).encode()).hexdigest()}",
                    add_all=True,
                    services=local_added
                )

                local_added = []  # Reset the local added list after creating a PR

            if counter == self.BATCH_SIZE:
                logging.info(f"Processed {self.BATCH_SIZE} services. Stopping for this run.")
                break # Stop after processing 30 services for this run
            else:
                logging.info(f"Processed {counter} services so far. Continuing to process more services...")
                

        # Save the completed services list
        logging.info("All services processed.")

    def complete_service(self, service_name: str, service_info: dict, created: bool):
        """
        Mark a service as completed and save its information.
        """
        self.completed_services[self.to_camel(service_name)] = service_info
        self.completed_services[self.to_camel(service_name)]['created'] = created
        logging.info(f"Service {service_name} marked as completed.")

        with open(self.COMPLETED_SERVICE_PATH, "w") as completed_services_file_handle:
            completed_services_file_handle.write(json.dumps(self.completed_services, indent=2))

    def to_camel(self, s: str) -> str:
        """
        Convert a phrase like 'I am ok' → 'iAmOk' (lower camel-case).

        • Splits on any non-alphanumeric boundary.
        • Keeps digits.
        • First token → lowercase; subsequent tokens → Capitalized.
        """
        words = [w for w in re.split(r'[^0-9A-Za-z]+', s) if w]
        if not words:
            return ""
        head, *tail = words
        return head.lower() + "".join(w.capitalize() for w in tail)


JSON_RESPONSE_SCHEMA = {
    "file_name": "{{service_name}}.py",
    "service": "{{service_name}}",
    "code": "string",
    "logo": "string",
    "branch_name": "string",
    "web_app": "boolean"
}

class ServiceResponseSchema(BaseModel):

    file_name: str
    service: str
    code: str
    logo: str
    branch_name: str
    web_app: bool

if __name__ == "__main__":

    logging.info("Starting service generation...")

    github_pr_creator = GithubPRCreator(
        github_client = Github(os.getenv("GH_TOKEN")),
        repo_name = "JTSG1/GreyhoundDash",
        base_branch = "main"
    )

    openai = OpenAI(base_url=os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1"), api_key=os.getenv("OPENAI_API_KEY"))

    serviceGenerator = ServiceGenerator(
        openai_client = OpenAI(),
        github_pr_creator = github_pr_creator
    )
    serviceGenerator.iterate_services()

    logging.info("Ended service generation.")