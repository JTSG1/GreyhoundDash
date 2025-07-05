from services.service_base import ServiceBase

class ServiceAlfrescoCommunityEdition(ServiceBase):
    """
    Alfresco Community Edition
    
    """
    id: str = 'alfrescoCommunityEdition'
    name: str = 'Alfresco Community Edition'
    description: str = 'An open-source Enterprise Content Management (ECM) system that manages all the content within an enterprise and provides the services and controls that manage this content.'
    tags: list[str] = ['content management', 'open-source', 'enterprise', 'ECM']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Alfresco Community Edition is a web application.
        web_app = True
        return super().render()