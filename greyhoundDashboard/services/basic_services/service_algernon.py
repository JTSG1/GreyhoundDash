from services.service_base import ServiceBase

class ServiceAlgernon(ServiceBase):
    """
    🐙 Algernon
    """
    id: str = 'algernon'
    name: str = 'Algernon'
    description: str = 'A lightweight and powerful service for building highly interactive dashboards and visualizations, designed for performance and simplicity.'
    tags: list[str] = ['dashboards', 'visualization', 'interactive', 'lightweight']

    def get(self) -> ServiceBase:
        super().get()
        return self
