from services.service_base import ServiceBase

class ServiceAdmidio(ServiceBase):
    """
    🎟️ Admidio
    """
    id: str = 'admidio'
    name: str = 'Admidio'
    description: str = 'A free open-source membership management software that assists organizations in managing their members, events, and finances.'
    tags: list[str] = ['membership', 'management', 'open-source', 'software']

    def get(self) -> ServiceBase:
        super().get()
        return self
    
    
    @classmethod
    def register(cls) -> None:
        super().register()
