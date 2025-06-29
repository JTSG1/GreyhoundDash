from services.service_base import ServiceBase

class Service0AD(ServiceBase):
    """
    🏛️ 0 A.D.
    """
    id: str = '0ad'
    name: str = '0 A.D.'
    description: str = 'A free, open-source real-time strategy game of ancient warfare, developed by Wildfire Games.'
    tags: list[str] = ['real-time strategy', 'open-source', 'cross-platform', 'historical', 'multiplayer']

    def get(self) -> ServiceBase:
        super().get()
        return self

    @classmethod
    def register(cls) -> None:
        super().register()

    @property
    def logo(self) -> str:
        return 'https://play0ad.com/wp-content/uploads/2021/04/0ad-logo.svg'

    @property
    def web_app(self) -> bool:
        return True
