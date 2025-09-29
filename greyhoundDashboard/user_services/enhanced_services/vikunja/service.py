from user_services.service_base import ServiceBase, EnhancedServiceBase

import requests
import json
import logging

logger = logging.getLogger(__name__)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from greyhoundDashboard.user_services.models import RegisteredService


class ServiceVikunja(EnhancedServiceBase):

    """
    📤 < Work!
    """    
    id = "vikunja"
    name:str = 'Vikunja'
    description:str = 'An open-source, self-hosted task management application that helps you plan, organize, and manage your personal or team projects efficiently.'
    tags: list[str] = ['productivity', 'task management', 'kanban', 'self-hosted', 'todo']
    enhanced_auth_fields: list[str] = ['username', 'password']
    is_enhanced: bool = True

    def __init__(self, registered_service: "RegisteredService"):
        """
        Initialize the enhanced service with the base service.
        """
        super().__init__(registered_service)
        
        self.state = {}
        self.username = registered_service.auth_fields["username"]
        self.password = registered_service.auth_fields["password"]
        self.url = registered_service.url if registered_service.url else None
        self.jwt = None

    def _get_jwt(self):

        result = requests.post(
            f"{self.url}/api/v1/login",
            json={"Username": self.username, "Password": self.password},
        )

        self.jwt = result.json().get("token")

    def _get_tasks(self):
        headers = {
            "Authorization": f"Bearer {self.jwt}",
            "Content-Type": "application/json",
        }
        result = requests.get(
            f"{self.url}/api/v1/tasks/all",
            headers=headers,
        )

        return result.json() if result.status_code == 200 else []
  
    def get(self) -> ServiceBase:

        super().get()

        if self.state["up"]:

            self._get_jwt()
            tasks = self._get_tasks()

            active_tasks = len([x for x in tasks if not x["done"]])
            done_tasks = len([x for x in tasks if x["done"]])

            self.state.update({
                "active": active_tasks,
                "done": done_tasks
            })

        return self


__all__ = [
    "ServiceVikunja",
]