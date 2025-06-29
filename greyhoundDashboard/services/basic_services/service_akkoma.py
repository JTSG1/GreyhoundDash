from services.service_base import ServiceBase

class ServiceAkkoma(ServiceBase):
    """
    🔊 Akkoma
    """
    id: str = 'akkoma'
    name: str = 'Akkoma'
    description: str = 'Akkoma is a self-hosted social network platform that emphasizes community, open-source, and decentralized control.'
    tags: list[str] = ['social', 'decentralized', 'open-source', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self
