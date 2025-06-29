from services.service_base import ServiceBase

class ServiceActivePieces(ServiceBase):
    """
    🤖 Activepieces
    """
    id: str = 'activepieces'
    name: str = 'Activepieces'
    description: str = 'An automation platform that connects apps and services to automate workflows with ease.'
    tags: list[str] = ['automation', 'workflows', 'integration', 'no-code']

    def get(self) -> ServiceBase:
        super().get()
        return self
