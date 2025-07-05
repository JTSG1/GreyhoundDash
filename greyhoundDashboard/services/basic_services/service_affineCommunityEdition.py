from services.service_base import ServiceBase

class ServiceAffineCommunityEdition(ServiceBase):
    """
    AFFiNE Community Edition
    ([affine.pro](https://affine.pro/?utm_source=openai))
    """
    id: str = 'affineCommunityEdition'
    name: str = 'AFFiNE Community Edition'
    description: str = 'An open-source, all-in-one workspace integrating documents, whiteboards, and databases with AI capabilities, designed to enhance creativity and productivity.'
    tags: list[str] = ['productivity', 'collaboration', 'open-source', 'AI', 'workspace']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Override the render method if a custom template is needed.
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
