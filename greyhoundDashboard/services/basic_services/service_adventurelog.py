from services.service_base import ServiceBase

class ServiceAdventureLog(ServiceBase):
    """
    🌍 AdventureLog
    """
    id: str = 'adventurelog'
    name: str = 'AdventureLog'
    description: str = 'An open-source, self-hosted travel tracker and trip planner designed to help you document and plan your journeys.'
    tags: list[str] = ['travel', 'tracker', 'trip planner', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for AdventureLog
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
        # Additional registration logic for AdventureLog
        pass
