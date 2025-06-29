from services.service_base import ServiceBase

class ServiceAnonaddy(ServiceBase):
    """
    🛡️ AnonAddy
    """
    id: str = 'anonaddy'
    name: str = 'AnonAddy'
    description: str = 'A privacy-focused email forwarding service that allows you to create aliases to protect your real email address.'
    tags: list[str] = ['privacy', 'email', 'security', 'anonymity']

    def get(self) -> ServiceBase:
        super().get()
        return self
