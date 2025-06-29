from services.service_base import ServiceBase

class ServiceAirtrail(ServiceBase):
    """
    🚀 Airtrail
    """
    id: str = 'airtrail'
    name: str = 'Airtrail'
    description: str = 'A seamless platform for monitoring and observability, providing powerful features for effective data handling and insights.'
    tags: list[str] = ['monitoring', 'observability', 'data-handling']

    def get(self) -> ServiceBase:
        super().get()
        return self
