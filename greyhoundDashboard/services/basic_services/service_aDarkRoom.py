from services.service_base import ServiceBase

class ServiceADarkRoom(ServiceBase):
    """
    🏰 aDarkRoom
    """
    id: str = 'adarkroom'
    name: str = 'aDarkRoom'
    description: str = 'A text-based adventure and survival game where players explore a mysterious world and gather resources to survive.'
    tags: list[str] = ['game', 'text-adventure', 'survival', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
