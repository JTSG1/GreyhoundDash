from core.services.service_base import ServiceBase, EnhancedServiceBase

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


class ServiceNavidrome(EnhancedServiceBase):

    """
    🎸 < Music!
    """
    id:str = 'navidrome'
    name:str = 'Navidrome'
    description:str = 'A self hosted music server with Subsonic API.',
    tags: list[str] = ['music', 'entertainment'],
    enhanced_auth_fields: list[str] = ['username', 'password']
    is_enhanced: bool = True


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


class ServiceVikunja(EnhancedServiceBase):

    """
    📤 < Work!
    """    
    id = "vikunja"
    name:str = 'Vikunja'
    description:str = 'An open-source, self-hosted task management application that helps you plan, organize, and manage your personal or team projects efficiently.',
    tags: list[str] = ['productivity', 'task management', 'kanban', 'self-hosted', 'todo'],
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
