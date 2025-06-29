from services.service_base import ServiceBase

class ServiceActivePieces(ServiceBase):
    """
    🧩 ActivePieces
    """
    id: str = 'activepieces'
    name: str = 'ActivePieces'
    description: str = 'A powerful automation platform that enables you to connect various web services and automate workflows with ease.'
    tags: list[str] = ['automation', 'integration', 'no-code', 'workflow']

    def get(self) -> ServiceBase:
        super().get()
        return self
