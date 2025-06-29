from greyhoundDashboard.services.service_base import ServiceBase

class AcpAdminService(ServiceBase):
    id = 'acpAdmin'
    name = 'ACP Admin'
    description = 'Service integration for ACP Admin dashboard.'
    tags = ['admin', 'dashboard']
    up_check = False

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        # Custom logic for checking the service availability can be added here
        return super().up_check()  # Use base class check as default

# Register the service
AcpAdminService.register()