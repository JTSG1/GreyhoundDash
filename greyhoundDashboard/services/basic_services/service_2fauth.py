from services.service_base import ServiceBase

class Service2FAuth(ServiceBase):
    """
    🔐 2FAuth
    """
    id: str = '2fauth'
    name: str = '2FAuth'
    description: str = 'A simple 2FA (Two-Factor Authentication) setup and management tool for adding an extra layer of security to applications.'
    tags: list[str] = ['security', 'authentication', 'two-factor', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
