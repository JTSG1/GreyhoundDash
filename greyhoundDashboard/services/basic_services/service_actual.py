from greyhoundDashboard.services.service_base import ServiceBase


class ActualService(ServiceBase):
    id = 'actual'
    name = 'Actual Budget'
    description = 'A budgeting tool that helps manage personal financial needs.'
    tags = ['finance', 'budgeting']
    up_check = False

    def __init__(self, registered_service):
        super().__init__(registered_service)

    @classmethod
    def register(cls) -> None:
        super().register()


# Register the service
ActualService.register()