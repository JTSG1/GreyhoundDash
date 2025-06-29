from services.service_base import ServiceBase

class ServiceAlfIo(ServiceBase):
    """
    🎟️ Alf.io
    """
    id: str = 'alfio'
    name: str = 'Alf.io'
    description: str = 'A ticketing and event management platform designed for ease of use, flexibility, and scalability.'
    tags: list[str] = ['ticketing', 'event management', 'scalable', 'flexible', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self
