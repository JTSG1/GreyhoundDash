from services.service_base import ServiceBase

class ServiceActivityWatch(ServiceBase):
    """
    ⌚ ActivityWatch
    """
    id: str = 'activitywatch'
    name: str = 'ActivityWatch'
    description: str = 'An open-source application for tracking how you spend your time on your computer, providing insights into your daily activities.'
    tags: list[str] = ['productivity', 'tracking', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
