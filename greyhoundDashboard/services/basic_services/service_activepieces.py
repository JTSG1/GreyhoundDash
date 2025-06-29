from greyhoundDashboard.services.service_base import ServiceBase

class ActivePiecesService(ServiceBase):
    id = 'activepieces'
    name = 'Activepieces'
    description = 'An automation service for connecting different applications.'
    tags = ['automation', 'integration', 'workflow']
    up_check = True

    def __init__(self, registered_service):
        super().__init__(registered_service)
        self.api_key = registered_service.api_key if hasattr(registered_service, 'api_key') else None

    def up_check(self):
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'}
            request = requests.get(self.registered_service.url, headers=headers, timeout=3)
            return request.status_code == 200
        except Exception:
            return False

    @classmethod
    def register(cls) -> None:
        super().register()