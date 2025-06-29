from services.service_base import ServiceBase

class ServiceActivepieces(ServiceBase):
    """
    🤖 Activepieces
    """
    id: str = 'activepieces'
    name: str = 'Activepieces'
    description: str = 'An open-source, AI-first automation platform that enables users to create and manage workflows by connecting various applications and services, offering both no-code and code-based solutions.'
    tags: list[str] = ['automation', 'AI', 'open-source', 'no-code', 'workflow']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for Activepieces can be added here
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
        # Additional registration logic for Activepieces can be added here
