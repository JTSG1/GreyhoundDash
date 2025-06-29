from services.service_base import ServiceBase

class ServiceADarkRoom(ServiceBase):
    """
    🕹️ aDarkRoom
    """
    id: str = 'adarkroom'
    name: str = 'aDarkRoom'
    description: str = 'A text-based adventure game that immerses players in a dark and mysterious world, adding elements of survival and exploration.'
    tags: list[str] = ['game', 'text-based', 'adventure', 'survival']

    def get(self) -> ServiceBase:
        super().get()
        return self
    
    def up_check(self):
        # Custom logic for checking if the aDarkRoom service is up
        return True  # Placeholder return value.
    
    @classmethod
    def register(cls) -> None:
        super().register()
