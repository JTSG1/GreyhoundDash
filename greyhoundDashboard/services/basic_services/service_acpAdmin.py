from services.service_base import ServiceBase

class ServiceAcpAdmin(ServiceBase):
    """
    ACP Admin
    """
    id: str = 'acp-admin'
    name: str = 'ACP Admin'
    description: str = 'A platform for managing various administrative tasks within ACP, facilitating efficient workflow management and team collaboration.'
    tags: list[str] = ['administration', 'workflow', 'management', 'collaboration']

    def get(self) -> ServiceBase:
        super().get()
        return self
