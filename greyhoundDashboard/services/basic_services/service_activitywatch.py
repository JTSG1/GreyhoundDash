from services.service_base import ServiceBase

class ServiceActivityWatch(ServiceBase):
    """
    ⏰ ActivityWatch
    """
    id: str = 'activitywatch'
    name: str = 'ActivityWatch'
    description: str = 'A self-hosted time tracking tool that helps you to log your productivity and manage your time efficiently.'
    tags: list[str] = ['time tracking', 'productivity', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

