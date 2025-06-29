from greyhoundDashboard.services.service_base import ServiceBase

class Service0AD(ServiceBase):
    id = '0ad'
    name = '0 A.D.'
    description = 'A free, open-source, historical real-time strategy game.'
    tags = ['gaming', 'strategy', 'open-source']

    def __init__(self, registered_service):
        super().__init__(registered_service)

    @classmethod
    def register(cls) -> None:
        super().register()

