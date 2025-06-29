from services.service_base import ServiceBase

class Service2FAuth(ServiceBase):
    """
    🔑 2FAuth
    """
    id: str = '2fauth'
    name: str = '2FAuth'
    description: str = 'A simple and effective Two-Factor Authentication as a Service (2FAaaS), designed to protect your applications with two-step verification.'
    tags: list[str] = ['authentication', 'security', '2FA', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
