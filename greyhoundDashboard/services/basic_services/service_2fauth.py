from greyhoundDashboard.services.service_base import ServiceBase

class TwoFactorAuthService(ServiceBase):
    id = '2fauth'
    name = 'Two Factor Authentication'
    description = 'Service for adding Two Factor Authentication to applications.'
    tags = ['security', 'authentication', '2FA']
    up_check: bool = True

    def __init__(self, registered_service):
        super().__init__(registered_service)
        self.api_key = registered_service.api_key  # Example field for enhanced auth

    def up_check(self):
        try:
            response = requests.get(self.registered_service.url, params={'api_key': self.api_key}, timeout=3)
            return response.status_code in [200, 401, 403]
        except Exception:
            return False

    @classmethod
    def register(cls) -> None:
        super().register()
