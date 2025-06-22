from abc import abstractmethod
from importlib.resources import files
from django.shortcuts import render
from django.template import Context, Template
from pathlib import Path
from django.utils.safestring import mark_safe

import requests

class ServiceBase:

    id: str = None
    name: str = None
    description: str = ""
    tags: list[str] = []
    up_check: bool = False
    is_enhanced: bool = False
    enhanced_auth_fields: list[str] = []

    def __init__(self, registered_service):
        self.state = {}
        self.registered_service = registered_service

    def get(self) -> "ServiceBase":
        """
        get the service integration.
        """
        self.state['up'] = self.up_check()

        return self

    def up_check(self):

        try:
            request = requests.get(self.registered_service.url, timeout=3)

            if request.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            return False
        
        return False

    def render(self) -> str:

        # template_path = Path(__file__).parent / "templates" / "components" / "enhanced-services" / f"{self.id}.html"

        template_path = files(".".join(self.__module__.split('.')[0:2])).joinpath(
            f"{self.id}.html"
        )

        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, encoding="utf-8") as fh:
            template_string = fh.read()

        template = Template(template_string)

        return mark_safe(template.render(Context({"state": self.state})))
    
    @classmethod
    def register(cls) -> None:

        from core.services.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            is_enhanced=cls.is_enhanced,
            enhanced=cls,
            enhanced_auth_fields=[]
        ))


class EnhancedServiceBase(ServiceBase):

    is_enhanced: bool = True
    enhanced_auth_fields: list[str] = []

    def __init__(self, registered_service):
        super().__init__(registered_service)

    @classmethod
    def register(cls) -> None:

        from core.services.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            is_enhanced=cls.is_enhanced,
            enhanced=cls,
            enhanced_auth_fields=[]
        ))
