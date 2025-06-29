from services.service_base import ServiceBase

class ServiceActivityWatch(ServiceBase):
    """
    🕒 ActivityWatch
    """
    id: str = 'activitywatch'
    name: str = 'ActivityWatch'
    description: str = 'An open-source, privacy-first time tracking application that monitors how you spend time on your devices.'
    tags: list[str] = ['time tracking', 'productivity', 'open-source', 'privacy', 'cross-platform']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for ActivityWatch
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
        # Additional registration logic for ActivityWatch
        pass
