from user_services.service_base import ServiceBase

class ServiceAdmidio(ServiceBase):
    """
    Admidio
    """
    id: str = 'admidio'
    name: str = 'Admidio'
    description: str = 'A free open-source user management system designed for organizations and groups, offering features like member lists, event management, and photo albums.'
    tags: list[str] = ['user management', 'membership management', 'open-source', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Admidio is a web-based application, so we can render its interface directly.
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()

    @classmethod
    def is_web_app(cls) -> bool:
        return True
