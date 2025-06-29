from services.service_base import ServiceBase

class ServiceActual(ServiceBase):
    """
    Budget tracking and visualization tool
    """
    id: str = 'actual'
    name: str = 'Actual'
    description: str = 'An open-source budget tracking application that helps you visualize your expenses and manage your finances effectively.'
    tags: list[str] = ['budgeting', 'finance', 'open-source', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self
