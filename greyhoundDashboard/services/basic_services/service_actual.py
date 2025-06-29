from greyhoundDashboard.services.service_base import ServiceBase

class ActualService(ServiceBase):
    id = 'actual'
    name = 'Actual Budget'
    description = 'A budget management tool.'
    tags = ['budget', 'finance', 'management']
    up_check = False

    def __init__(self, registered_service):
        super().__init__(registered_service)

    # Additional methods for ActualService can be defined here
