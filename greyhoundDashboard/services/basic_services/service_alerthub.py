from services.service_base import ServiceBase

class ServiceAlerthub(ServiceBase):
    """
    🚨 AlertHub
    """
    id: str = 'alerthub'
    name: str = 'AlertHub'
    description: str = 'An open-source alerting platform that integrates with various messaging systems to provide adaptable alert management.'
    tags: list[str] = ['alerting', 'monitoring', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

