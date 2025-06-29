from services.service_base import ServiceBase

class ServiceActivityWatch(ServiceBase):
    """
    ⏱️ ActivityWatch
    """
    id: str = 'activitywatch'
    name: str = 'ActivityWatch'
    description: str = 'An open-source, privacy-first, cross-platform time tracker that monitors application usage and provides insights into your digital life.'
    tags: list[str] = ['time tracking', 'productivity', 'open-source', 'cross-platform', 'privacy-first']
    logo: str = 'https://activitywatch.net/logo.png'
    web_app: bool = True

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
