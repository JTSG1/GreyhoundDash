from services.service_base import ServiceBase

class ServiceADarkRoom(ServiceBase):
    """
    🕹️ aDarkRoom
    """
    id: str = 'adarkroom'
    name: str = 'aDarkRoom'
    description: str = 'An immersive text-based adventure game that offers a unique experience through exploration and survival.'
    tags: list[str] = ['game', 'adventure', 'text-based', 'rpg', 'exploration']

    def get(self) -> ServiceBase:
        super().get()
        return self
