from greyhoundDashboard.services.service_base import ServiceBase


class AccentService(ServiceBase):
    id = 'accent'
    name = 'Accent Reviews'
    description = 'This service integrates with Accent to provide reviews and insights.'
    tags = ['reviews', 'insights', 'accent']

    def __init__(self, registered_service):
        super().__init__(registered_service)

    @classmethod
    def register(cls) -> None:
        super().register()

    def up_check(self):
        # Override base up_check if specific behavior is needed
        return super().up_check()

    def render(self) -> str:
        # You can customize rendering if necessary
        return super().render()