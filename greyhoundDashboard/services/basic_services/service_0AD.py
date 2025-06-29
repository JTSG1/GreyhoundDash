from greyhoundDashboard.services.service_base import ServiceBase

class Service0AD(ServiceBase):
    id = '0ad'
    name = '0 A.D.'
    description = '0 A.D. is a free, open-source, historical real-time strategy game developed by Wildfire Games.'
    tags = ['Game', 'Strategy', 'Open Source']
    up_check = True

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def custom_method(self):  # Example of a potential customization
        return f'{self.name} is currently {"up" if self.state.get("up") else "down"}. '

# Register the service
Service0AD.register()