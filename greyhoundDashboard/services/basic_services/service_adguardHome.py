from services.service_base import ServiceBase

class ServiceAdGuardHome(ServiceBase):
    """
    🛡️ AdGuard Home
    """
    id: str = 'adguard_home'
    name: str = 'AdGuard Home'
    description: str = 'A network-wide ads and trackers blocking DNS server that protects your devices and ensures a faster, safer internet experience.'
    tags: list[str] = ['dns', 'ad-blocking', 'network', 'privacy']

    def get(self) -> ServiceBase:
        super().get()
        return self
