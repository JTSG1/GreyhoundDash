from services.service_base import ServiceBase

class ServiceActual(ServiceBase):
    """
    💰 Actual Budget
    """
    id: str = 'actual'
    name: str = 'Actual Budget'
    description: str = 'A privacy-focused budgeting app that helps users manage their finances effectively, offering features like envelope-style budgeting, multi-device sync, and optional end-to-end encryption.'
    tags: list[str] = ['budgeting', 'finance', 'personal-finance', 'money', 'privacy', 'envelope-budgeting']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for Actual Budget
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
        # Additional registration logic for Actual Budget
        pass
