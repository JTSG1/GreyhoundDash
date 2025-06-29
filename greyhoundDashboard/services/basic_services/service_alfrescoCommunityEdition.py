from services.service_base import ServiceBase

class ServiceAlfrescoCommunityEdition(ServiceBase):
    """
    Alfresco Community Edition
    """
    id: str = 'alfrescoCommunityEdition'
    name: str = 'Alfresco Community Edition'
    description: str = 'An open-source enterprise content management system that provides a robust platform for managing documents, web content, and digital assets.'
    tags: list[str] = ['content management', 'open-source', 'documents', 'collaboration']

    def get(self) -> ServiceBase:
        super().get()
        return self
