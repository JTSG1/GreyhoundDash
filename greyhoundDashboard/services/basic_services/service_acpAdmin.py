from greyhoundDashboard.services.service_base import ServiceBase

class ACPAdminService(ServiceBase):
    id = 'acpAdmin'
    name = 'ACP Admin'
    description = 'Service for managing ACP admin functionalities.'
    tags = ['admin', 'management', 'acp']
    up_check = True

    def __init__(self, registered_service):
        super().__init__(registered_service)

    # You can add additional methods or overrides if necessary
