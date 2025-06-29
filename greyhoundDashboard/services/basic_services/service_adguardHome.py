from greyhoundDashboard.services.service_base import ServiceBase

class AdGuardHomeService(ServiceBase):
    id = 'adguard_home'
    name = 'AdGuard Home'
    description = 'A network-wide ad blocker that allows you to block ads at the DNS level.'
    tags = ['ad-blocker', 'network', 'privacy']
    up_check = True

    def __init__(self, registered_service):
        super().__init__(registered_service)

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

    def specific_method(self):
        # Additional functionality specific to AdGuard Home can be implemented here
        pass