from greyhoundDashboard.services.service_base import ServiceBase

class Service4gaBoards(ServiceBase):
    id = '4gaBoards'
    name = '4gaboards Service'
    description = 'Integration for the 4gaboards service.'
    tags = ['forum', 'community', '4gaboards']
    up_check = False

    def __init__(self, registered_service):
        super().__init__(registered_service)

    @classmethod
    def register(cls) -> None:
        super().register()

    def get(self) -> 'Service4gaBoards':
        super().get()
        self.state['extra_info'] = self.fetch_extra_info()
        return self

    def fetch_extra_info(self):
        # Implement fetching additional information specific to 4gaboards
        return {'info': 'Extra information about 4gaboards'}

# Register the service upon import
Service4gaBoards.register()