from services.service_base import ServiceBase

class ServiceActual(ServiceBase):
    """
    Actual Budget
    """
    id: str = 'actual'
    name: str = 'Actual'
    description: str = 'A budgeting tool designed to help users manage their finances and track their spending visually.'
    tags: list[str] = ['budgeting', 'finance', 'personal finance', 'web application']

    def get(self) -> ServiceBase:
        super().get()
        return self
