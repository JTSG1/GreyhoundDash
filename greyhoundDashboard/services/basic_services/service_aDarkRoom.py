from greyhoundDashboard.services.service_base import ServiceBase

class aDarkRoom(ServiceBase):
    id = 'aDarkRoom'
    name = 'A Dark Room'
    description = 'A text-based adventure game where you build a camp and explore'
    tags = ['game', 'adventure', 'text-based']
    up_check = True

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        try:
            request = requests.get(self.registered_service.url, timeout=3)
            return request.status_code == 200
        except Exception:
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
