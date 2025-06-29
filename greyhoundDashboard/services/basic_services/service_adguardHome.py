from services.service_base import ServiceBase

class ServiceAdGuardHome(ServiceBase):
    """
    🛡️ AdGuard Home
    """
    id: str = 'adguard_home'
    name: str = 'AdGuard Home'
    description: str = 'An open-source software, which allows you to block ads and trackers at the network level.'
    tags: list[str] = ['dns', 'ad-blocking', 'open-source', 'network', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self
