
from abc import abstractmethod
from django.shortcuts import render
import requests
import json
import logging

logger = logging.getLogger(__name__)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.models import RegisteredService

class ServiceBase:

    id: str = None
    name: str = None
    description: str = ""
    tags: list[str] = []
    up_check: bool = False

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
    def register(cls):

        from core.services.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            enhanced=None,
            enhanced_auth_fields=[]
        ))

class EnhancedServiceBase(ServiceBase):

    is_enhanced: bool = True
    enhanced_auth_fields: list[str] = []

    @classmethod
    def register(cls):

        from core.services.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            enhanced=cls,
            enhanced_auth_fields=cls.enhanced_auth_fields
        ))

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


class ServiceNavidrome(ServiceBase):

    """
    🎸 < Music!
    """
    id = "navidrome"

    def __init__(self, registered_service: "RegisteredService"):

        self.state = {}
        self.username = registered_service.auth_fields["username"]
        self.password = registered_service.auth_fields["password"]
        self.url = registered_service.url if registered_service.url else None

    def get_now_playing(self):

        response = requests.get(
            f"{self.url}/rest/getNowPlaying?u={self.username}&p={self.password}&f=json&v=1.16.1&c=greyhound"
        )

        try:

            first_return = response.json()["subsonic-response"]["nowPlaying"]["entry"][0]

            import base64

            response_image = requests.get(
                f"{self.url}/rest/getCoverArt?u={self.username}&p={self.password}&f=json&v=1.16.1&c=greyhound&id={first_return["coverArt"]}"
            )

            encoded = base64.b64encode(response_image.content).decode('utf-8')
            encoded = f"data:image/png;base64,{encoded}"

        except:

            first_return = {
                "artist" : "Nothing On",
                "album" : "",
                "title" : ""
            }

            encoded = None


        return first_return, encoded

    def get(self) -> ServiceBase:

        super().get()

        if self.state["up"]:

            logger.info("Getting Navidrome data")

            first_return, encoded = self.get_now_playing()

            self.state.update({
                "artist" : first_return["artist"],
                "album" : first_return["album"],
                "title" : first_return["title"],
                "art" : encoded
            })

        return self


class ServiceVikunja(ServiceBase):

    """
    📤 < Work!
    """    
    id = "vikunja"

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
