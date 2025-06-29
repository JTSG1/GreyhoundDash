from services.service_base import ServiceBase

class ServiceAcpAdmin(ServiceBase):
    """
    🏢 ACP Admin
    """
    id: str = 'acp_admin'
    name: str = 'ACP Admin'
    description: str = 'A service for administration tasks and management in various environments.'
    tags: list[str] = ['admin', 'management', 'web-app', 'tool']

    def get(self) -> ServiceBase:
        super().get()
        return self

