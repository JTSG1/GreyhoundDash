from greyhoundDashboard.services.service_base import ServiceBase

class Service2FAuth(ServiceBase):
    """
    🔐 2FAuth
    """
    id: str = '2fauth'
    name: str = '2FAuth'
    description: str = 'A 2FAuthentication service that helps you secure your applications with Two-Factor Authentication.'
    tags: list[str] = ['authentication', '2FA', 'security', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
