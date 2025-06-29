from services.service_base import ServiceBase

class ServiceAmusewiki(ServiceBase):
    """
    A·Muse·Wiki
    ([amusewiki.org](https://amusewiki.org/?utm_source=openai))
    """
    id: str = 'amusewiki'
    name: str = 'A·Muse·Wiki'
    description: str = 'A library-oriented wiki engine and publishing platform that supports high-quality output formats like EPUB and PDF, with a focus on long-term archiving and offline editing.'
    tags: list[str] = ['wiki engine', 'publishing platform', 'open-source', 'offline editing', 'EPUB', 'PDF']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Override the render method to provide custom rendering logic if needed.
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
        # Additional registration logic can be added here if necessary.
