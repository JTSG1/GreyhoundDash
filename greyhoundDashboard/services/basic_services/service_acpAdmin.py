from services.service_base import ServiceBase

class ServiceAcpAdmin(ServiceBase):
    """
    📋 ACP Admin
    """
    id: str = 'acp_admin'
    name: str = 'ACP Admin'
    description: str = 'A web administration portal for managing system configurations and user accounts.'
    tags: list[str] = ['admin', 'management', 'portal', 'web']

    def get(self) -> ServiceBase:
        super().get()
        return self
