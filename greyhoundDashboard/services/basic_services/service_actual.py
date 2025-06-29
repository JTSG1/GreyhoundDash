from services.service_base import ServiceBase

class ServiceActual(ServiceBase):
    """
    🏦 Actual Budget
    """
    id: str = 'actual'
    name: str = 'Actual Budget'
    description: str = 'An open-source budgeting tool designed to help users manage their finances effectively.'
    tags: list[str] = ['budgeting', 'finance', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
