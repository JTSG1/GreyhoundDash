from services.service_base import ServiceBase

class ServiceAffineCommunityEdition(ServiceBase):
    """
    🔧 Affine Community Edition
    """
    id: str = 'affineCommunityEdition'
    name: str = 'Affine Community Edition'
    description: str = 'Affine is an open-source integrated platform for managing data workflows, projects, and teams seamlessly.'
    tags: list[str] = ['data management', 'open-source', 'community edition', 'collaboration']

    def get(self) -> ServiceBase:
        super().get()
        return self
