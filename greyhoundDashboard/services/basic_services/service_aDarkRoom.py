from services.service_base import ServiceBase

class ServiceADarkRoom(ServiceBase):
    """
    🕯️ A Dark Room
    """
    id: str = 'adarkroom'
    name: str = 'A Dark Room'
    description: str = 'A minimalist text-based adventure game that unfolds a mysterious world from a single button press.'
    tags: list[str] = ['text-based', 'adventure', 'minimalist', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for A Dark Room
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()

    @classmethod
    def logo(cls) -> str:
        return 'https://github.com/doublespeakgames/adarkroom/raw/main/img/logo.png'

    @classmethod
    def web_app(cls) -> bool:
        return True
