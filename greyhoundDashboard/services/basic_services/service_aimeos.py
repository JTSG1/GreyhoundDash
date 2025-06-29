from services.service_base import ServiceBase

class ServiceAimeos(ServiceBase):
    """
    🛒 Aimeos
    """
    id: str = 'aimeos'
    name: str = 'Aimeos'
    description: str = 'Aimeos is an open-source e-commerce framework that provides a powerful toolset for building complex applications with ease.'
    tags: list[str] = ['e-commerce', 'open-source', 'framework', 'PHP']

    def get(self) -> ServiceBase:
        super().get()
        return self
