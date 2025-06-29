from greyhoundDashboard.services.service_base import ServiceBase


class Service0AD(ServiceBase):
    id = '0ad'
    name = '0 A.D.'
    description = 'A historical real-time strategy game'
    tags = ['game', 'strategy', 'open-source']
    up_check = True

    def __init__(self, registered_service):
        super().__init__(registered_service)

