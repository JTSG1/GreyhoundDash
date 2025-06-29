from services.service_base import ServiceBase

class Service2FAuth(ServiceBase):
    """
    🔐 2FAuth
    """
    id: str = '2fauth'
    name: str = '2FAuth'
    description: str = 'A two-factor authentication service that helps secure applications by enforcing additional authentication factors.'
    tags: list[str] = ['security', 'authentication', '2FA', 'web-auth']

    def get(self) -> ServiceBase:
        super().get()
        return self
