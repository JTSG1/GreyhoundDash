from services.service_base import ServiceBase

class ServiceActual(ServiceBase):
    """
    💰 Actual Budget
    """
    id: str = 'actual'
    name: str = 'Actual Budget'
    description: str = 'A local-first, privacy-focused personal finance app that utilizes envelope budgeting to help users manage their finances effectively.'
    tags: list[str] = ['budgeting', 'personal finance', 'privacy', 'envelope budgeting', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for Actual Budget can be added here
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()

    @classmethod
    def logo(cls) -> str:
        return 'https://www.vectorlogo.zone/logos/actualbudget/actualbudget-icon.svg'

    @classmethod
    def web_app(cls) -> bool:
        return True