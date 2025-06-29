from services.service_base import ServiceBase

class ServiceAdGuardHome(ServiceBase):
    """
    🛡 AdGuard Home
    """
    id: str = 'adguard_home'
    name: str = 'AdGuard Home'
    description: str = 'A network-wide software for blocking ads and tracking. AdGuard Home acts as a DNS server, filtering requests to ensure ad-free browsing.'
    tags: list[str] = ['ad-blocking', 'dns', 'privacy', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self

