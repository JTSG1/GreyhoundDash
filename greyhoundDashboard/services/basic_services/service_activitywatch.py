from greyhoundDashboard.services.service_base import ServiceBase


class ActivityWatchService(ServiceBase):
    id = 'activitywatch'
    name = 'ActivityWatch'
    description = 'A service to track user activity on different applications and websites.'
    tags = ['monitoring', 'productivity', 'analytics']

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        try:
            request = requests.get(self.registered_service.url + '/api/ping', timeout=3)
            return request.status_code == 200
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
            service_class=cls,
            enhanced_auth_fields=[]
        ))