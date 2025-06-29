from services.service_base import ServiceBase

class ServiceAdguardHome(ServiceBase):
    """
    🚀 AdGuard Home
    """
    id: str = 'adguard_home'
    name: str = 'AdGuard Home'
    description: str = 'An open-source software for blocking ads and tracking in your home network.'
    tags: list[str] = ['ad-blocking', 'network', 'privacy', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
