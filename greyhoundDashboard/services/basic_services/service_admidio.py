from services.service_base import ServiceBase

class ServiceAdmidio(ServiceBase):
    """
    🎉 Admidio
    """
    id: str = 'admidio'
    name: str = 'Admidio'
    description: str = 'Admidio is a free and open-source member management software that helps organizations manage their members, payments, and events.'
    tags: list[str] = ['member management', 'open-source', 'non-profit', 'community']

    def get(self) -> ServiceBase:
        super().get()
        return self
