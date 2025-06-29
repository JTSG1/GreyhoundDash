from greyhoundDashboard.services.service_base import ServiceBase


class TwoFactorAuthService(ServiceBase):
    id = '2fauth'
    name = 'Two Factor Authentication'
    description = 'Service for two-factor authentication.'
    tags = ['security', 'authentication']
    up_check = False

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        try:
            response = requests.get(self.registered_service.url + '/status', timeout=3)
            return response.status_code == 200
        except Exception as e:
            return False

    @classmethod
    def register(cls) -> None:
        from core.services.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            is_enhanced=False,
            service_class=cls
        ))

