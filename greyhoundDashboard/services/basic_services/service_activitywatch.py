from services.service_base import ServiceBase

class ServiceActivityWatch(ServiceBase):
    """
    ⏰ ActivityWatch
    """
    id: str = 'activitywatch'
    name: str = 'ActivityWatch'
    description: str = 'An open-source, self-hosted time tracking application that helps you keep track of your digital activities.'
    tags: list[str] = ['time tracking', 'self-hosted', 'open-source', 'monitoring']

    def get(self) -> ServiceBase:
        super().get()
        return self
