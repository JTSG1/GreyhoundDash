# package greyhoundDashboard.services.service_base
# -*- coding: utf-8 -*-
# This file is part of Greyhound Dashboard.

from importlib.resources import files
from django.template import Context, Template
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
        """Check if the service is up and log the status if it has changed."""
        from user_services.models import RegisteredServiceLog

        def log_status(is_up: bool) -> None:
            """Create a health check log entry."""
            RegisteredServiceLog(
                message=is_up,
                type=RegisteredServiceLog.LogType.HEALTHCHECK,
                registered_service=self.registered_service
            ).save()

        # Get last check status
        try:
            last_check = RegisteredServiceLog.objects.filter(
                registered_service=self.registered_service,
                type=RegisteredServiceLog.LogType.HEALTHCHECK
            ).last()
        except Exception:
            last_check = None

        # Check service status
        try:
            request = requests.get(self.registered_service.url, timeout=3)
            is_up = request.status_code in [200, 401, 403]
        except Exception:
            is_up = False

        # Log only if status changed or no previous check exists
        should_log = (
            not last_check or 
            (last_check.message == 'True' and not is_up) or
            (last_check.message == 'False' and is_up)
        )

        if should_log:
            log_status(is_up)
        
        return is_up
    
    @classmethod
    def register(cls) -> None:

        from user_services.registry.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            is_enhanced=cls.is_enhanced,
            service_class=cls,
            enhanced_auth_fields=[]
        ))


class EnhancedServiceBase(ServiceBase):

    is_enhanced: bool = True
    enhanced_auth_fields: list[str] = []

    def __init__(self, registered_service):
        super().__init__(registered_service)

    @classmethod
    def register(cls) -> None:

        from user_services.registry.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            is_enhanced=cls.is_enhanced,
            service_class=cls,
            enhanced_auth_fields=cls.enhanced_auth_fields
        ))

    def render(self) -> str:
        
        template_path = files(".".join(self.__module__.split('.')[0:2])).joinpath(
            self.name,
            f"{self.id}.html"
        )

        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, encoding="utf-8") as fh:
            template_string = fh.read()

        template = Template(template_string)

        return mark_safe(template.render(Context({"state": self.state})))
    
