from dataclasses import dataclass, field
from enum import Enum
from typing import Type
# from .services import ServiceBase, ServicePortainer, ServiceNavidrome, ServiceVikunja

@dataclass
class ServiceDefinition:
    name: str
    description: str
    tags: list[str] = field(default_factory=list)
    enhanced: object | None = None
    enhanced_auth_fields: list[str] = field(default_factory=list)

class ServiceDefinitions:

    definition_dict = {
        # 'portainer': ServiceDefinition(
        #     name='Portainer',
        #     description='A lightweight management UI which allows you to easily manage your Docker containers.',
        #     tags=['docker', 'management'],
        #     enhanced=ServicePortainer,
        #     enhanced_auth_fields=['username', 'password']
        # ),
        # 'navidrome': ServiceDefinition(
        #     name='Navidrome',
        #     description='A self hosted music server with Subsonic API.',
        #     tags=['music', 'entertainment'],
        #     enhanced=ServiceNavidrome,
        #     enhanced_auth_fields=['username', 'password']
        # ),
        # 'vikunja': ServiceDefinition(
        #     name='Vikunja',
        #     description='An open-source, self-hosted task management application that helps you plan, organize, and manage your personal or team projects efficiently.',
        #     tags=['productivity', 'task management', 'kanban', 'self-hosted', 'todo'],
        #     enhanced=ServiceVikunja,
        #     enhanced_auth_fields=['username', 'password']
        # ),
        # 'proxmox': ServiceDefinition(
        #     name="Proxmox",
        #     description='An open-source virtualization management platform for running and managing virtual machines and containers using KVM and LXC technologies.',
        #     tags=['virtualization', 'infrastructure', 'hypervisor', 'containers', 'kvm', 'self-hosted']
        # ),
        # 'openwebui': ServiceDefinition(
        #     name="Open WebUI",
        #     description="A sleek, self-hosted interface for interacting with large language models like ChatGPT, supporting local backends such as Ollama and LM Studio.",
        #     tags=["AI", "LLM", "chatbot", "self-hosted", "open-source"]
        # ),
        # 'custom': ServiceDefinition(
        #     name='Custom',
        #     description='A custom service that can be defined by the user.',
        #     tags=['custom']
        # ),
    }

    @classmethod
    def choices(cls):
        return tuple((key, defn.name) for key, defn in cls.definition_dict.items())

    @classmethod
    def register(cls, key:str, definition: ServiceDefinition):
        cls.definition_dict[key] = definition

    @classmethod
    def get_definition(cls, service_type: str) -> ServiceDefinition | None:
        """
        Get the service definition by its identifier string (e.g., 'portainer').
        Returns None if the service is not found.
        """
        return cls.definition_dict.get(service_type, None)
