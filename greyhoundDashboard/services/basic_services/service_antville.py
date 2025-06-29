from services.service_base import ServiceBase

class ServiceAntville(ServiceBase):
    """
    🐜 Antville
    """
    id: str = 'antville'
    name: str = 'Antville'
    description: str = 'An open-source, high-performance weblog hosting system written in server-side JavaScript, capable of hosting tens of thousands of blogs.'
    tags: list[str] = ['blogging', 'content-management', 'open-source', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for Antville can be added here
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
        # Additional registration logic for Antville can be added here
