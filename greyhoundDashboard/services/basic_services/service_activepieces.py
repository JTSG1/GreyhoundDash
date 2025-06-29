from services.service_base import ServiceBase

class ServiceActivePieces(ServiceBase):
    """
    ✨ ActivePieces
    """
    id: str = 'activepieces'
    name: str = 'ActivePieces'
    description: str = 'An automation platform to connect various apps and services without code, enabling workflow automation through pieces that interact with APIs.'
    tags: list[str] = ['automation', 'no-code', 'workflow', 'integration', 'productivity']

    def get(self) -> ServiceBase:
        super().get()
        return self
