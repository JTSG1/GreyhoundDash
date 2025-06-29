from services.service_base import ServiceBase

class ServiceAcpAdmin(ServiceBase):
    """
    Admin Control Panel
    """
    id: str = 'acpAdmin'
    name: str = 'acpAdmin'
    description: str = 'A centralized admin panel for managing various services and resources within a system.'
    tags: list[str] = ['admin', 'management', 'control panel', 'dashboard']

    def get(self) -> ServiceBase:
        super().get()
        return self
