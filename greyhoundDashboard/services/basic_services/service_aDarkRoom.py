from services.service_base import ServiceBase

class ServiceADarkRoom(ServiceBase):
    """
    🕹️ A Dark Room
    """
    id: str = 'adarkroom'
    name: str = 'A Dark Room'
    description: str = 'A minimalist text-based role-playing game that begins with the player awakening in a cold, dark room after a mysterious event.'
    tags: list[str] = ['game', 'text-based', 'adventure', 'minimalist']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for A Dark Room
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
