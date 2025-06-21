from abc import abstractmethod
from django.shortcuts import render

import requests

class ServiceBase:

    id: str = None
    name: str = None
    description: str = ""
    tags: list[str] = []
    up_check: bool = False
    is_enhanced: bool = False
    enhanced_auth_fields: list[str] = []

    def __init__(self, registered_service: "RegisteredService"):
        self.url = None
        self.state = {}

    def get(self) -> "ServiceBase":
        """
        get the service integration.
        """
        self.state['up'] = self.up_check()

        return self

    def up_check(self):

        try:
            request = requests.get(self.url, timeout=3)

            if request.status_code == 200:
                return True
        except:
            return False
        
        return False

    def render(self) -> str:
        return render(None, f"components/enhanced-services/{self.id}.html", {"state": self.state}).text

    @classmethod
    def register(cls) -> None:

        from core.services.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            is_enhanced=cls.is_enhanced,
            enhanced=None,
            enhanced_auth_fields=[]
        ))


class EnhancedServiceBase(ServiceBase):

    is_enhanced: bool = True
    enhanced_auth_fields: list[str] = []

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
