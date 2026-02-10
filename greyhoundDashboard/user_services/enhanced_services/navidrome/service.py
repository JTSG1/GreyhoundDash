from user_services.service_base import ServiceBase, EnhancedServiceBase

import requests
import json
import logging

logger = logging.getLogger(__name__)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from greyhoundDashboard.user_services.models import RegisteredService

class ServiceNavidrome(EnhancedServiceBase):

    """
    🎸 < Music!
    """
    id:str = 'navidrome'
    name:str = 'Navidrome'
    description:str = 'A self hosted music server with Subsonic API.'
    tags: list[str] = ['music', 'entertainment']
    enhanced_auth_fields: list[str] = ['username', 'password']
    is_enhanced: bool = True


    def __init__(self, registered_service: "RegisteredService"):

        super().__init__(registered_service)

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