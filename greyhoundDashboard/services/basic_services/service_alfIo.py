from services.service_base import ServiceBase

class ServiceAlfIo(ServiceBase):
    """
    🎟️ Alf.io
    """
    id: str = 'alfio'
    name: str = 'Alf.io'
    description: str = 'Alf.io is an open-source platform for creating, managing, and conducting events, offering ticketing and registration solutions.'
    tags: list[str] = ['event management', 'ticketing', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
