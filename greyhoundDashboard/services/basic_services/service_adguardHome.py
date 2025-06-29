from greyhoundDashboard.services.service_base import ServiceBase

# AdGuard Home Service implementation

class AdGuardHomeService(ServiceBase):
    id = 'adguard_home'
    name = 'AdGuard Home'
    description = 'AdGuard Home is a network-wide software for blocking ads and trackers.'
    tags = ['dns', 'network', 'ad-blocking']

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        # Custom logic to check if AdGuard Home is up
        return super().up_check()  # Use the base implementation

    @classmethod
    def register(cls) -> None:
        super().register()  # Register the service using the base class method

# Register the service
AdGuardHomeService.register()