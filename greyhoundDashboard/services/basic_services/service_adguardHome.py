from services.service_base import ServiceBase

class ServiceAdGuardHome(ServiceBase):
    """
    AdGuard Home
    ([adguard.com](https://adguard.com/en/adguard-home/overview.html?utm_source=openai))
    """
    id: str = 'adguardHome'
    name: str = 'AdGuard Home'
    description: str = 'A network-wide software for blocking ads and tracking, providing a unified solution for blocking ads and trackers on all devices within your network.'
    tags: list[str] = ['network-wide', 'ad blocking', 'privacy', 'self-hosted', 'open-source']
    up_check: bool = True
    is_enhanced: bool = False
    enhanced_auth_fields: list[str] = []

    def get(self) -> ServiceBase:
        super().get()
        return self

    @classmethod
    def register(cls) -> None:
        super().register()

    @property
    def logo(self) -> str:
        return 'https://adguard.com/favicon.ico'

    @property
    def web_app(self) -> bool:
        return True
