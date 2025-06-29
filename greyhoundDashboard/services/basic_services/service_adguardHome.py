from services.service_base import ServiceBase

class ServiceAdGuardHome(ServiceBase):
    """
    🛡️ AdGuard Home
    """
    id: str = 'adguard_home'
    name: str = 'AdGuard Home'
    description: str = 'A network-wide software for blocking ads and tracking, providing filtering features for various protocols.'
    tags: list[str] = ['ad-blocking', 'network', 'privacy', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
