from services.service_base import ServiceBase

class ServiceAmpache(ServiceBase):
    """
    📀 Ampache
    """
    id: str = 'ampache'
    name: str = 'Ampache'
    description: str = 'Ampache is a web-based media library and music streaming application, designed to facilitate and enhance your music collection through a powerful and intuitive interface.'
    tags: list[str] = ['media', 'music', 'streaming', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
