from services.service_base import ServiceBase

class ServiceAmuseWiki(ServiceBase):
    """
    📚 AmuseWiki
    """
    id: str = 'amusewiki'
    name: str = 'AmuseWiki'
    description: str = 'A free and open-source platform for creating and sharing interactive narratives and knowledge associated with various topics.'
    tags: list[str] = ['wiki', 'knowledge', 'open-source', 'collaboration']

    def get(self) -> ServiceBase:
        super().get()
        return self
