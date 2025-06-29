from greyhoundDashboard.services.service_base import ServiceBase

class ActivePiecesService(ServiceBase):
    id = 'activepieces'
    name = 'ActivePieces'
    description = 'Automation platform that helps you connect apps and automate workflows.'
    tags = ['automation', 'integration', 'workflow']

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        try:
            response = requests.get(self.registered_service.url + '/health', timeout=3)
            return response.status_code == 200
        except Exception:
            return False

    @classmethod
    def register(cls) -> None:
        super().register()