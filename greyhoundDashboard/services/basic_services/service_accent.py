from services.service_base import ServiceBase

class ServiceAccent(ServiceBase):
    """
    📊 Accent
    """
    id: str = 'accent'
    name: str = 'Accent'
    description: str = 'A platform that provides customer feedback and review management services, helping businesses enhance their reputation and understanding of customer experiences.'
    tags: list[str] = ['reviews', 'feedback', 'customer-engagement', 'reputation-management']

    def get(self) -> ServiceBase:
        super().get()
        return self
