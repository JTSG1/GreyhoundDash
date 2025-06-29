from services.service_base import ServiceBase

class ServiceAlerthub(ServiceBase):
    """
    📬 AlertHub
    """
    id: str = 'alerthub'
    name: str = 'AlertHub'
    description: str = 'A simple alert system that supports various integrations for notifying users through multiple channels.'
    tags: list[str] = ['alerts', 'notification', 'monitoring', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self
