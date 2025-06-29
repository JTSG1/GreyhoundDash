from services.service_base import ServiceBase

class ServiceAdGuardHome(ServiceBase):
    """
    AdGuard Home
    ([adguard.com](https://adguard.com/en/adguard-home/overview.html?utm_source=openai))
    """
    id: str = 'adguardHome'
    name: str = 'AdGuard Home'
    description: str = 'A network-wide software for blocking ads and tracking, providing a user-friendly web interface for managing network-wide filtering.'
    tags: list[str] = ['network-wide', 'ad-blocking', 'privacy', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # AdGuard Home provides a web interface for managing network-wide filtering.
        # ([adguard.com](https://adguard.com/en/adguard-home/overview.html?utm_source=openai))
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()

    @property
    def web_app(self) -> bool:
        return True
