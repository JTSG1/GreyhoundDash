from services.service_base import ServiceBase

class ServiceADarkRoom(ServiceBase):
    """
    🕹️ A Dark Room
    """
    id: str = 'adarkroom'
    name: str = 'A Dark Room'
    description: str = 'A minimalist text adventure game where you start in a dark room and light a fire, with the story evolving from there.'
    tags: list[str] = ['game', 'text-adventure', 'minimalist', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for A Dark Room
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
        # Additional registration logic for A Dark Room
        pass
