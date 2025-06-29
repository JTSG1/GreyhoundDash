from greyhoundDashboard.services.service_base import ServiceBase


class Service4gaBoards(ServiceBase):
    id = '4gaBoards'
    name = '4GA Boards'
    description = 'Service for 4GA Boards integration'
    tags = ['forum', 'community', '4ga']
    up_check = False

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        try:
            request = requests.get('https://4gaboards.com', timeout=3)
            return request.status_code in [200, 401, 403]
        except Exception:
            return False

    @classmethod
    def register(cls) -> None:
        super().register()