from services.service_base import ServiceBase

class ServiceAdminer(ServiceBase):
    """
    🗄️ Adminer
    """
    id: str = 'adminer'
    name: str = 'Adminer'
    description: str = 'A full-featured database management tool written in PHP, allowing easy access to databases.'
    tags: list[str] = ['database', 'management', 'PHP', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
