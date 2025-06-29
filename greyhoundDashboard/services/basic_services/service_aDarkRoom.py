from services.service_base import ServiceBase

class ServiceADarkRoom(ServiceBase):
    """
    🕹️ A Dark Room
    """
    id: str = 'adarkroom'
    name: str = 'A Dark Room'
    description: str = 'A minimalist text adventure game where you start in a dark room and light a fire, leading to an evolving story and gameplay.'
    tags: list[str] = ['game', 'text-adventure', 'minimalist', 'browser-based']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Assuming the game has a web interface, we can render it directly.
        return "<iframe src='https://adarkroom.doublespeakgames.com' width='800' height='600'></iframe>"

    @classmethod
    def register(cls) -> None:
        from core.services.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            is_enhanced=cls.is_enhanced,
            service_class=cls,
            enhanced_auth_fields=[]
        ))
