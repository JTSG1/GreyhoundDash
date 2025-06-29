from services.service_base import ServiceBase

class Service0AD(ServiceBase):
    """
    ⚔️ 0 A.D.
    """
    id: str = '0ad'
    name: str = '0 A.D.'
    description: str = 'A free, open-source, historical real-time strategy game that allows players to build ancient civilizations.'
    tags: list[str] = ['gaming', 'strategy', 'open-source', 'historical']

    def get(self) -> ServiceBase:
        super().get()
        return self
