from greyhoundDashboard.services.service_base import ServiceBase

class aDarkRoom(ServiceBase):
    id = 'aDarkRoom'
    name = 'A Dark Room'
    description = 'A text-based adventure game that starts with a dark room.'
    tags = ['game', 'text-based', 'adventure']

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        # Custom logic for A Dark Room service health check can be added here
        return super().up_check()  # Calls the base class method

    def render(self) -> str:
        # Any custom rendering logic for A Dark Room can be added here
        return super().render()  # Calls the base class method

# Uncomment the following line if you want to register this service automatically when the module is imported
# aDarkRoom.register()