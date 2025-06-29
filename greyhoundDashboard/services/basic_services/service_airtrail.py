from services.service_base import ServiceBase

class ServiceAirtrail(ServiceBase):
    """
    🛰 Airtrail
    """
    id: str = 'airtrail'
    name: str = 'Airtrail'
    description: str = 'A tool for tracking and visualizing your network performance, providing insights for better operational activities.'
    tags: list[str] = ['network monitoring', 'visualization', 'analytics', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self
