from services.service_base import ServiceBase

class Service2FAuth(ServiceBase):
    """
    2FAuth
    """
    id: str = '2fauth'
    name: str = '2FAuth'
    description: str = 'A simple and easy-to-use two-factor authentication solution, allowing integration with various services.'
    tags: list[str] = ['2fa', 'authentication', 'security', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

