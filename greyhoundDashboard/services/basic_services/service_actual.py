from services.service_base import ServiceBase

class ServiceActual(ServiceBase):
    """
    💰 Actual Budget
    """
    id: str = 'actual'
    name: str = 'Actual Budget'
    description: str = 'A local-first, privacy-focused personal finance app that utilizes envelope budgeting to help users manage their finances effectively.'
    tags: list[str] = ['finance', 'budgeting', 'privacy', 'open-source']

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
