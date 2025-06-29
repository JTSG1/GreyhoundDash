from services.service_base import ServiceBase

class ServiceAleph(ServiceBase):
    """
    🗄️ Aleph
    """
    id: str = 'aleph'
    name: str = 'Aleph'
    description: str = 'A platform for collaborative investigations, enabling journalists to aggregate and share datasets, documents, and discover links between entities.'
    tags: list[str] = ['investigation', 'data-sharing', 'journalism', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

