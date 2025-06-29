from services.service_base import ServiceBase

class ServiceAcpAdmin(ServiceBase):
    """
    CSA Admin
    """
    id: str = 'acpAdmin'
    name: str = 'CSA Admin'
    description: str = 'A web-based platform designed to simplify the management of Community Supported Agriculture (CSA) organizations, offering features like member management, delivery scheduling, automated billing, and more.'
    tags: list[str] = ['CSA management', 'web application', 'open-source', 'agriculture']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Assuming the logo is available at a specific path
        self.state['logo'] = '/path/to/logo.png'
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
        # Additional registration logic if needed
