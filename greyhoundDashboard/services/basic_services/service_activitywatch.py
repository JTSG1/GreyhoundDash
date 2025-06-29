from services.service_base import ServiceBase

class ServiceActivityWatch(ServiceBase):
    """
    🕒 ActivityWatch
    """
    id: str = 'activitywatch'
    name: str = 'ActivityWatch'
    description: str = 'An open-source time tracking software that helps you keep track of your activities and time usage across various applications and websites.'
    tags: list[str] = ['time tracking', 'productivity', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

