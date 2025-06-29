from services.service_base import ServiceBase

class Service4gaBoards(ServiceBase):
    """
    4GaBoards Service
    """
    id: str = '4gaboards'
    name: str = '4GaBoards'
    description: str = 'A comprehensive platform for board games management and community engagement, offering tools to enhance gameplay experience.'
    tags: list[str] = ['board games', 'management', 'community', 'gaming']

    def get(self) -> ServiceBase:
        super().get()
        return self
