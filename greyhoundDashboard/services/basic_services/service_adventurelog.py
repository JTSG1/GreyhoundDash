from services.service_base import ServiceBase

class ServiceAdventureLog(ServiceBase):
    """
    📖 AdventureLog
    """
    id: str = 'adventurelog'
    name: str = 'AdventureLog'
    description: str = 'A tool for tracking and sharing your adventures, helping you keep a record of your experiences and journeys.'
    tags: list[str] = ['tracking', 'adventure', 'journaling', 'experience']

    def get(self) -> ServiceBase:
        super().get()
        return self
