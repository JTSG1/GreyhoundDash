from services.service_base import ServiceBase

class ServiceActivityWatch(ServiceBase):
    """
    ⏳ ActivityWatch
    """
    id: str = 'activitywatch'
    name: str = 'ActivityWatch'
    description: str = 'An open-source, self-hosted timesheet application that tracks your activity and provides insights into your software usage.'
    tags: list[str] = ['time tracking', 'open-source', 'self-hosted', 'productivity']

    def get(self) -> ServiceBase:
        super().get()
        return self
