from openai import OpenAI
import json
import re
from pydantic import BaseModel
from github import Github
import os
import subprocess
from hashlib import md5
import requests

class ServiceGenerator:
    """
    This class is responsible for generating service code based on a template and provided parameters.
    It uses the OpenAI API to generate the code and save it to a file.
    """
    completed_service_path = "tooling/awesome_selfhosted_services_completed.json"

    def __init__(self, prompt_template_path: str = "tooling/service_generation_prompt.txt"):
        self.client = OpenAI()
        self.prompt_template = open(prompt_template_path, "r").read()
        self.service_data = self.__parse_retrieved_service_data()
        self.completed_services = self.__get_completed_list()

        self.github_client = Github(os.getenv("GH_TOKEN"))
        self.repo = self.github_client.get_repo("JTSG1/GreyhoundDash")
        self.base = self.repo.get_branch("main")

    def replace_template_variables(
        self,
        template: str, 
        base_class_file: str, 
        base_class_name: str,
        implementation_samples: str,
        json_schema: dict,
        service_name: str, 
        service_homepage: str) -> str: 
    
        template = template.replace("{% base_class_file %}", base_class_file)
        template = template.replace("{% base_class_name %}", base_class_name)
        template = template.replace("{% implementation_samples %}", implementation_samples)
        template = template.replace("{% service_name %}", service_name)
        template = template.replace("{% service_homepage %}", service_homepage)
        template = template.replace("{% json_schema %}", str(json_schema))

        return template

    def generate_service_code(self, service_name: str, homepage: str) -> str:

        prompt = self.replace_template_variables(
            self.prompt_template,
            base_class_file=open("greyhoundDashboard/services/service_base.py", "r").read(),
            base_class_name="ServiceBase",
            implementation_samples=open("greyhoundDashboard/services/basic_services/service_grafana.py", "r").read(),
            json_schema=json.dumps(JSON_RESPONSE_SCHEMA, indent=2),
            service_name=service_name,
            service_homepage=homepage
        )

        response = self.client.responses.parse(
            model="gpt-4o-mini",
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
            text_format=ServiceResponseSchema
        )

        content = response.output_parsed

        # Save the generated code to a file
        with open(f"greyhoundDashboard/services/basic_services/{content.file_name}", "w") as code_file:
            code_file.write(content.code)

        # Save the logo to a file
        logo_url = content.logo
        # ignoring images for now
        

    def __parse_retrieved_service_data(self):

        with open("tooling/awesome_selfhosted_services.json", "r") as file:
            data = json.load(file)

        return data
    
    def __get_completed_list(self):

        try:
            with open(self.completed_service_path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {self.completed_service_path}. Returning an empty list.")
                    data = {}
        except FileNotFoundError:
            print(f"Completed services file not found at {self.completed_service_path}. Returning an empty list.")
            data = {}

        return data

    def iterate_services(self):
        """
        Iterate through the service data and generate code for each service.
        """
        
        counter = 0

        added_list_local = []

        for service_name, service_info in self.service_data.items():

            if self.completed_services.get(service_name):
                print(f"Service {service_name} already processed.")
                continue

            if service_name in self.completed_services:
                print(f"Service {service_name} already completed.")
                continue
            
            print(f"Generating code for {service_name}...")
            self.generate_service_code(service_name, service_info['homepage'])
            self.complete_service(
                service_name = service_info['name'],
                service_info = service_info
            )

            added_list_local.append(service_info['name'])

            counter += 1

            if counter % 10 == 0:

                print("Processed 10 services. Stopping for now to avoid rate limits. Creating a branch and raising a PR for the last 10 services...")

                self.create_branch_and_raise_pr(
                    branch_name=f"feat/service-generation-{counter}-{md5(''.join(added_list_local).encode()).hexdigest()}",
                    add_all=True,
                    services=added_list_local
                )

                added_list_local = []  # Reset the list for the next batch

            if counter == 30:
                break # Stop after processing 30 services for this run

        # Save the completed services list
        print("All services processed.")

    def complete_service(self, service_name: str, service_info: dict):
        """
        Mark a service as completed and save its information.
        """
        self.completed_services[self.to_camel(service_name)] = service_info
        print(f"Service {service_name} marked as completed.")

        with open(self.completed_service_path, "w") as completed_services_file_handle:
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

    def create_branch_and_raise_pr(self, branch_name: str, *, add_all: bool = True, services: list = None):
        """
        Create a new branch in the GitHub repository.
        """
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

        pr = self.repo.create_pull(                          # ⇦ GitHub API: POST /pulls :contentReference[oaicite:1]{index=1}
            title = f"Add new basic services from service generation {services[0]} to {services[-1]}",
            body  = f"This implements the following services: \n\n { '\n'.join(services) }",
            head  = branch_name,         # what you just created
            base  = "main",             # where you want it merged
            draft = False               # or True for a draft PR
        )

JSON_RESPONSE_SCHEMA = {
    "file_name": "{{service_name}}.py",
    "service": "{{service_name}}",
    "code": "string",
    "logo": "string",
    "branch_name": "string"
}

class ServiceResponseSchema(BaseModel):

    file_name: str
    service: str
    code: str
    logo: str
    branch_name: str

serviceGenerator = ServiceGenerator()
serviceGenerator.iterate_services()

print("FIN")