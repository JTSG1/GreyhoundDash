from services.service_base import ServiceBase

class ServiceAimeos(ServiceBase):
    """
    🛍️ Aimeos
    """
    id: str = 'aimeos'
    name: str = 'Aimeos'
    description: str = 'Aimeos is an open-source e-commerce framework based on PHP and Laravel that provides extensive support for various businesses and sales channels.'
    tags: list[str] = ['e-commerce', 'open-source', 'PHP', 'framework', 'shopping']

    def get(self) -> ServiceBase:
        super().get()
        return self
