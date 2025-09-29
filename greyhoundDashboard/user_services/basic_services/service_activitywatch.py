from user_services.service_base import ServiceBase

class ServiceActivityWatch(ServiceBase):
    """
    🕒 ActivityWatch
    """
    id: str = 'activitywatch'
    name: str = 'ActivityWatch'
    description: str = 'An open-source, privacy-first time tracker that monitors application usage and provides insights into digital habits.'
    tags: list[str] = ['time tracking', 'productivity', 'open-source', 'privacy-first']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for ActivityWatch
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()

    @property
    def web_app(self) -> bool:
        return True
