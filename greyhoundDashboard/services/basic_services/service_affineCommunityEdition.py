from services.service_base import ServiceBase

class ServiceAffineCommunityEdition(ServiceBase):
    """
    Affine Community Edition
    """
    id: str = 'affineCommunityEdition'
    name: str = 'Affine Community Edition'
    description: str = 'An open-source data analysis and visualization platform that allows users to work intuitively with their data to generate insights.'
    tags: list[str] = ['data analysis', 'visualization', 'open-source', 'community edition']

    def get(self) -> ServiceBase:
        super().get()
        return self

