from services.service_base import ServiceBase, EnhancedServiceBase

import requests
import json
import logging

logger = logging.getLogger(__name__)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.models import RegisteredService

class ServicePortainer(EnhancedServiceBase):

    """
    🫙 < Container!
    """    
    id:str = 'portainer'
    name:str = 'Portainer'
    description:str = 'A lightweight management UI which allows you to easily manage your Docker containers.',
    tags: list[str] = ['docker', 'management'],
    enhanced_auth_fields: list[str] = ['username', 'password']
    is_enhanced: bool = True

    def __init__(self, registered_service: "RegisteredService"):
        """
        Initialize the enhanced service with the base service.
        """
        self.state = {}
        self.username = registered_service.auth_fields["username"]
        self.password = registered_service.auth_fields["password"]
        self.url = registered_service.url if registered_service.url else None
        self.jwt = None

    def _get_jwt(self):

        result = requests.post(
            f"{self.url}/api/auth",
            json={"Username": self.username, "Password": self.password},
        )

        self.jwt = result.json().get("jwt")

    def _get_environment(self):
        headers = {
            "Authorization": f"Bearer {self.jwt}",
            "Content-Type": "application/json",
        }
        result = requests.get(
            f"{self.url}/api/endpoints",
            headers=headers,
        )   

        return result.json() if result.status_code == 200 else []

    def _get_containers(self, env_id):
        headers = {
            "Authorization": f"Bearer {self.jwt}",
            "Content-Type": "application/json",
        }
        result = requests.get(
            f"{self.url}/api/endpoints/{env_id}/docker/containers/json?all=true",
            headers=headers,
        )

        return result.json() if result.status_code == 200 else []
    
    def get(self) -> ServiceBase:

        super().get()

        if self.state["up"]:

            self._get_jwt()
            envs = self._get_environment()
            containers_across_envs = []
            for env in envs:
                containers = self._get_containers(env["Id"])
                containers_across_envs.extend(containers)

            self.state.update({
                "running": len([container for container in containers_across_envs if container["State"] == "running"]),
                "exited": len([container for container in containers_across_envs if container["State"] == "exited"]),
            })

        return self