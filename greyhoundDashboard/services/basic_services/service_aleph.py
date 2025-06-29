from services.service_base import ServiceBase

class ServiceAleph(ServiceBase):
    """
    🗺️ Aleph
    """
    id: str = 'aleph'
    name: str = 'Aleph'
    description: str = 'A tool for working with and visualizing large sets of data, particularly useful for journalists and researchers.'
    tags: list[str] = ['data visualization', 'investigation', 'journalism', 'research']

    def get(self) -> ServiceBase:
        super().get()
        return self
