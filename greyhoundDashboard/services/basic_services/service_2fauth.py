from services.service_base import ServiceBase

class Service2FAuth(ServiceBase):
    """
    🔐 2FAuth
    """
    id: str = '2fauth'
    name: str = '2FAuth'
    description: str = 'A web-based self-hosted alternative to One Time Passcode (OTP) generators like Google Authenticator, designed for both mobile and desktop.'
    tags: list[str] = ['security', 'authentication', '2FA', 'self-hosted', 'open-source']
    logo: str = 'https://2fauth.app/logo.png'
    web_app: bool = True

    def get(self) -> ServiceBase:
        super().get()
        return self

    @classmethod
    def register(cls) -> None:
        from core.services.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            is_enhanced=cls.is_enhanced,
            service_class=cls,
            enhanced_auth_fields=cls.enhanced_auth_fields
        ))
