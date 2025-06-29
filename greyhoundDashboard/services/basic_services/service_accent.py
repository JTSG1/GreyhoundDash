from services.service_base import ServiceBase

class ServiceAccent(ServiceBase):
    """
    ✨ Accent
    """
    id: str = 'accent'
    name: str = 'Accent'
    description: str = 'Accent is a service for collecting and analyzing customer reviews from various platforms, providing insights for businesses to improve their services.'
    tags: list[str] = ['reviews', 'analytics', 'customer feedback', 'insights']

    def get(self) -> ServiceBase:
        super().get()
        return self
