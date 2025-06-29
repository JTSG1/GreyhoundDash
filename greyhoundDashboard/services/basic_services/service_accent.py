from greyhoundDashboard.services.service_base import ServiceBase

class ServiceAccent(ServiceBase):
    """
    🌟 Accent
    """
    id: str = 'accent'
    name: str = 'Accent'
    description: str = 'Accent provides insights and reviews on brands and services, helping users make informed decisions.'
    tags: list[str] = ['reviews', 'insights', 'user-feedback']

    def get(self) -> ServiceBase:
        super().get()
        return self
