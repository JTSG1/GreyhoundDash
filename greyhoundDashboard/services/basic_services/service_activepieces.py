from services.service_base import ServiceBase

class ServiceActivePieces(ServiceBase):
    """
    🚀 Activepieces
    """
    id: str = 'activepieces'
    name: str = 'Activepieces'
    description: str = 'An automation platform that integrates diverse applications and services, enabling seamless workflows and task automation.'
    tags: list[str] = ['automation', 'integration', 'workflows', 'no-code']

    def get(self) -> ServiceBase:
        super().get()
        return self
