from services.service_base import ServiceBase

class ServiceADarkRoom(ServiceBase):
    """
    🕹️ aDarkRoom
    """
    id: str = 'adarkroom'
    name: str = 'aDarkRoom'
    description: str = 'A text-based adventure game that provides an immersive experience of survival and exploration.'
    tags: list[str] = ['game', 'text-based', 'adventure', 'survival']

    def get(self) -> ServiceBase:
        super().get()
        return self
