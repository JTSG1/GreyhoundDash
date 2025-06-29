from services.service_base import ServiceBase

class ServiceActual(ServiceBase):
    """
    💰 Actual Budget
    """
    id: str = 'actual'
    name: str = 'Actual Budget'
    description: str = 'A privacy-focused, local-first personal finance app that utilizes envelope budgeting to help users manage their finances effectively.'
    tags: list[str] = ['budgeting', 'finance', 'privacy', 'local-first', 'open-source']
    up_check: bool = True

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
    def is_web_app(cls) -> bool:
        return True
