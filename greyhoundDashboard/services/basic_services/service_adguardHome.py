from greyhoundDashboard.services.service_base import ServiceBase

class AdGuardHomeService(ServiceBase):
    id = 'adguard_home'
    name = 'AdGuard Home'
    description = 'AdGuard Home is a network-wide software for blocking ads and trackers.'
    tags = ['adblocking', 'network', 'privacy']
    up_check = False  # Implement as needed if checks are required

    def __init__(self, registered_service):
        super().__init__(registered_service)

    @classmethod
    def register(cls) -> None:
        super().register()  # Call the base class register method

