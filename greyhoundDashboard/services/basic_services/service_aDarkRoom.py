from services.service_base import ServiceBase

class ServiceADarkRoom(ServiceBase):
    """
    🔦 aDarkRoom
    """
    id: str = 'adarkroom'
    name: str = 'aDarkRoom'
    description: str = 'A text-based adventure game that immerses you in a dark world, where you must gather resources, explore, and survive.'
    tags: list[str] = ['game', 'adventure', 'text-based', 'survival']

    def get(self) -> ServiceBase:
        super().get()
        return self
