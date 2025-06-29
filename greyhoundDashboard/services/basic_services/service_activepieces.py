from services.service_base import ServiceBase

class ServiceActivePieces(ServiceBase):
    """
    ⚡ ActivePieces
    """
    id: str = 'activepieces'
    name: str = 'ActivePieces'
    description: str = 'A powerful automation platform that connects apps and automates workflows without code, enhancing productivity.'
    tags: list[str] = ['automation', 'workflows', 'no-code', 'productivity']

    def get(self) -> ServiceBase:
        super().get()
        return self
