from greyhoundDashboard.services.service_base import ServiceBase

class ActivePiecesService(ServiceBase):
    id = "activepieces"
    name = "ActivePieces"
    description = "Activepieces is a no-code automation platform that enables users to connect apps and create custom workflows."
    tags = ["automation", "no-code", "integration"]

    def __init__(self, registered_service):
        super().__init__(registered_service)

    def up_check(self):
        # Here you can implement specific logic for checking if ActivePieces is up
        return super().up_check()  # Calling the base class up_check

    # You can add more specific methods or overrides as needed

ActivePiecesService.register()