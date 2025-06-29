from services.service_base import ServiceBase

class ServicePihole(ServiceBase):
    """
    🛡️ Pi-hole
    """
    id: str = 'pihole'
    name: str = 'Pi-hole'
    description: str = 'A network-wide ad blocker that acts as a DNS sinkhole to block ads, trackers, and malicious domains for all devices on your network.'
    tags: list[str] = ['network', 'ad-blocking', 'dns', 'privacy', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
