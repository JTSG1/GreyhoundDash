from services.service_base import ServiceBase

class ServiceActual(ServiceBase):
    """
    📝 Actual
    """
    id: str = 'actual'
    name: str = 'Actual'
    description: str = 'A user-friendly budgeting tool that integrates with your bank accounts to help you track expenses and savings effortlessly.'
    tags: list[str] = ['budgeting', 'finance', 'personal finance', 'money management']

    def get(self) -> ServiceBase:
        super().get()
        return self
