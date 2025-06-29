from services.service_base import ServiceBase

class ServiceAcpAdmin(ServiceBase):
    """
    🖥️ ACP Admin
    """
    id: str = 'acp_admin'
    name: str = 'ACP Admin'
    description: str = 'A central administration platform for ACP, providing user management, settings configuration, and dashboard access.'
    tags: list[str] = ['administration', 'management', 'dashboard', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self
