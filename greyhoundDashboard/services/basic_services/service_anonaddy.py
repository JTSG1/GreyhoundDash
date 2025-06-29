from services.service_base import ServiceBase

class ServiceAnonAddy(ServiceBase):
    """
    🛡️ AnonAddy
    """
    id: str = 'anonaddy'
    name: str = 'AnonAddy'
    description: str = 'An open-source anonymous email forwarding service that allows users to create unlimited email aliases to protect their real email addresses.'
    tags: list[str] = ['email', 'privacy', 'security', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for AnonAddy can be added here
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
        # Additional registration logic for AnonAddy can be added here
