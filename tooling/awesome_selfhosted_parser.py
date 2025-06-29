from bs4 import BeautifulSoup
import requests
import re

def fetch_awesome_selfhosted():
    url = "https://awesome-selfhosted.net/#software"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the page: {response.status_code}")
    return response.text

def to_camel(s: str) -> str:
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

def parse_awesome_selfhosted(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    services = {}
    skipped_services = []
    
    for section_software in soup.find_all('section', id='software'):

        sections = section_software.find_all("section")

        for section in sections:
            service_name = section.find('h3').text.strip().replace("#", "")
            service_description = section.find('p').text.strip() if section.find('p') else "No description available"
            service_homepage = section.find('a', class_='external-link')['href'] if section.find('a', class_='external-link') else None
            
            if not service_homepage:
                skipped_services.append(service_name)
                continue
            

            services[to_camel(service_name)] = {
                'name': service_name,
                'description': service_description,
                'homepage': service_homepage
            }
        
    if skipped_services:
        print(f"Skipped {len(skipped_services)} services without a homepage link: {', '.join(skipped_services)}")

    return services

result = parse_awesome_selfhosted(fetch_awesome_selfhosted())

with open("tooling/awesome_selfhosted_services.json", "w") as f:
    import json
    json.dump(result, f, indent=2)