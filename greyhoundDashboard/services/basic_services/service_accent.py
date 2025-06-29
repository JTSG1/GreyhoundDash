from services.service_base import ServiceBase

class ServiceAccent(ServiceBase):
    """
    🟡 Accent
    """
    id: str = 'accent'
    name: str = 'Accent'
    description: str = 'Accent is a modern reviews platform that provides insights and analytics to improve customer experiences.'
    tags: list[str] = ['reviews', 'analytics', 'customer-experience', 'insights']

    def get(self) -> ServiceBase:
        super().get()
        return self
