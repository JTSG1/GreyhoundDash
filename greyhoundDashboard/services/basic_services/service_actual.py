from services.service_base import ServiceBase

class ServiceActual(ServiceBase):
    """
    📊 Actual
    """
    id: str = 'actual'
    name: str = 'Actual'
    description: str = 'A budgeting application that helps users manage their finances intelligently and visually, offering insights and analysis.'
    tags: list[str] = ['budgeting', 'finance', 'tracking', 'web-app']

    def get(self) -> ServiceBase:
        super().get()
        return self
