from greyhoundDashboard.services.service_base import ServiceBase

class TwoFAuthService(ServiceBase):
    id = '2fauth'
    name = '2FAuth'
    description = 'Two-factor authentication service integration.'
    tags = ['authentication', 'security', '2fa']

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        try:
            response = requests.get(self.registered_service.url, timeout=5)
            return response.status_code in [200, 401]
        except requests.RequestException:
            return False

    @classmethod
    def register(cls) -> None:
        super().register()

# Registration of the service when the module is loaded
TwoFAuthService.register()