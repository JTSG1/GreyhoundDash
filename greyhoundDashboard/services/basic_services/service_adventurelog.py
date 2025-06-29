from services.service_base import ServiceBase

class ServiceAdventureLog(ServiceBase):
    """
    📖 AdventureLog
    """
    id: str = 'adventurelog'
    name: str = 'AdventureLog'
    description: str = 'A platform for documenting and sharing your adventures and experiences, allowing for a rich storytelling format.'
    tags: list[str] = ['adventure', 'blog', 'storytelling', 'sharing']

    def get(self) -> ServiceBase:
        super().get()
        return self
