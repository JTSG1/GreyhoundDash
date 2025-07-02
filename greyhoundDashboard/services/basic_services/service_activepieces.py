from services.service_base import ServiceBase

class ServiceActivepieces(ServiceBase):
    """
    🤖 Activepieces
    """
    id: str = 'activepieces'
    name: str = 'Activepieces'
    description: str = 'An open-source, no-code automation platform that enables users to create and manage workflows by connecting various applications and services, streamlining tasks across departments like marketing and sales.'
    tags: list[str] = ['automation', 'no-code', 'workflow', 'open-source', 'integration']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for Activepieces can be added here
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
        # Additional registration logic specific to Activepieces can be added here
