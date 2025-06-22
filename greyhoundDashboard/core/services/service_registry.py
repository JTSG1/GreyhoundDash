from dataclasses import dataclass, field
from enum import Enum
from typing import Type
# from .services import ServiceBase, ServicePortainer, ServiceNavidrome, ServiceVikunja

@dataclass
class ServiceDefinition:
    name: str
    description: str
    tags: list[str] = field(default_factory=list)
    is_enhanced: bool = False
    service_class: object | None = None
    enhanced_auth_fields: list[str] = field(default_factory=list)

class ServiceDefinitions:

    definition_dict: dict[ServiceDefinition] = {
       
    }

    @classmethod
    def choices(cls) -> tuple[tuple[str, str], ...]:
        return tuple((key, defn.name) for key, defn in cls.definition_dict.items())

    @classmethod
    def register(cls, key:str, definition: ServiceDefinition) -> None:
        cls.definition_dict[key] = definition

    @classmethod
    def get_definition(cls, service_type: str) -> ServiceDefinition | None:
        """
        Get the service definition by its identifier string (e.g., 'portainer').
        Returns None if the service is not found.
        """
        return cls.definition_dict.get(service_type, None)
