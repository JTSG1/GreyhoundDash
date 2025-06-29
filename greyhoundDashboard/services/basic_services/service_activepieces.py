from services.service_base import ServiceBase

class ServiceActivepieces(ServiceBase):
    """
    🤖 Activepieces
    """
    id: str = 'activepieces'
    name: str = 'Activepieces'
    description: str = 'An open-source, AI-first, no-code automation platform that enables teams to build automated workflows across various applications and services.'
    tags: list[str] = ['automation', 'AI', 'no-code', 'open-source', 'workflow']
    logo: str = 'https://www.activepieces.com/logo.png'
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
