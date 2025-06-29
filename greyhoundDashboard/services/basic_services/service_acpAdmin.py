from greyhoundDashboard.services.service_base import ServiceBase

class AcpAdminService(ServiceBase):
    id = 'acpAdmin'
    name = 'ACP Admin'
    description = 'Service integration for ACP Admin dashboard.'
    tags = ['admin', 'dashboard', 'acp']

    def __init__(self, registered_service):
        super().__init__(registered_service)
        self.registered_service.url = 'https://acp-admin.ch/'

    @classmethod
    def register(cls) -> None:
        super().register()

# Register the service
AcpAdminService.register()