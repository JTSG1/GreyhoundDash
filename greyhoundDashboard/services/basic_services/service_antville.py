from services.service_base import ServiceBase

class ServiceAntville(ServiceBase):
    """
    📖 Antville
    """
    id: str = 'antville'
    name: str = 'Antville'
    description: str = 'Antville is a community-driven content management system for building and managing individual websites or personal blogs.'
    tags: list[str] = ['cms', 'blogging', 'community-driven', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
