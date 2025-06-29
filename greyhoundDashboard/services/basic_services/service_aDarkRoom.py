from services.service_base import ServiceBase

class ServiceADarkRoom(ServiceBase):
    """
    🕹️ aDarkRoom
    """
    id: str = 'adarkroom'
    name: str = 'aDarkRoom'
    description: str = 'An incremental adventure game that immerses players in a dark and mysterious world full of exploration and story.'
    tags: list[str] = ['game', 'adventure', 'incremental', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
