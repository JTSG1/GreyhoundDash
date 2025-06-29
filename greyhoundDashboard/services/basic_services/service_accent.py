from services.service_base import ServiceBase

class ServiceAccent(ServiceBase):
    """
    📑 Accent
    """
    id: str = 'accent'
    name: str = 'Accent'
    description: str = 'Accent is a service for gathering and managing reviews to enhance customer satisfaction and brand reputation.'
    tags: list[str] = ['reviews', 'feedback', 'customer_satisfaction', 'web_app']

    def get(self) -> ServiceBase:
        super().get()
        return self
