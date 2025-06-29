from services.service_base import ServiceBase

class ServiceAdminer(ServiceBase):
    """
    🗄️ Adminer
    """
    id: str = 'adminer'
    name: str = 'Adminer'
    description: str = 'Adminer is a full-featured database management tool written in PHP. It provides a simple interface for managing databases.'
    tags: list[str] = ['database', 'management', 'php', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
