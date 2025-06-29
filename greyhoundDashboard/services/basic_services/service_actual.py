from greyhoundDashboard.services.service_base import ServiceBase

class ActualService(ServiceBase):
    id = 'actual'
    name = 'Actual Budget'
    description = 'Service for managing budget with Actual Budget.'
    tags = ['budget', 'finance']
    up_check = False

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        try:
            request = requests.get(self.registered_service.url, timeout=3)
            return request.status_code in [200, 401, 403]
        except Exception as e:
            return False

    @classmethod
    def register(cls) -> None:
        super().register()