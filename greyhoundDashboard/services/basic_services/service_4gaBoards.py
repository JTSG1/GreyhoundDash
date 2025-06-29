from greyhoundDashboard.services.service_base import ServiceBase

class Service4gaBoards(ServiceBase):
    id = '4gaBoards'
    name = '4GABoards'
    description = 'A service for accessing forums on 4gaboards.com'
    tags = ['forum', 'community', '4gaboards']

    def __init__(self, registered_service):
        super().__init__(registered_service)

    @classmethod
    def register(cls):
        from core.services.service_registry import ServiceDefinitions, ServiceDefinition
        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            is_enhanced=False,
            service_class=cls,
            enhanced_auth_fields=[]
        ))

# Registering the service
Service4gaBoards.register()