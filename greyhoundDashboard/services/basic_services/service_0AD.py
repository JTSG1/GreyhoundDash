from greyhoundDashboard.services.service_base import ServiceBase

class Service0AD(ServiceBase):
    id = '0AD'
    name = '0 A.D.'
    description = 'A free, open-source, historical real-time strategy game.'
    tags = ['game', 'strategy', 'open-source']

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        # Here you could implement a more specific check for the 0AD service
        return super().up_check()

# Register the service
Service0AD.register()