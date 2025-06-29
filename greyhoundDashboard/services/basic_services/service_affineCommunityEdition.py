from services.service_base import ServiceBase

class ServiceAffineCommunityEdition(ServiceBase):
    """
    AFFiNE Community Edition
    
    """
    id: str = 'affineCommunityEdition'
    name: str = 'AFFiNE Community Edition'
    description: str = 'An open-source, all-in-one workspace that integrates documents, whiteboards, and databases, designed to enhance creativity and productivity.'
    tags: list[str] = ['productivity', 'open-source', 'collaboration', 'knowledge-management']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Override the render method if a custom template is needed.
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()

    @property
    def web_app(self) -> bool:
        return True

    @property
    def logo(self) -> str:
        return 'URL_to_AFFiNE_logo_image'

    @property
    def branch_name(self) -> str:
        return 'main'