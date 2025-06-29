from greyhoundDashboard.services.service_base import ServiceBase

class aDarkRoomService(ServiceBase):
    id = 'adarkroom'
    name = 'A Dark Room'
    description = 'A text-based game that immerses you in a dark room.'
    tags = ['game', 'text-based']
    up_check = True  # Assuming it has a check to determine if the service is up

    def __init__(self, registered_service):
        super().__init__(registered_service)

    # Additional methods specific to aDarkRoom can be added here

# Registering the service
if __name__ == '__main__':
    aDarkRoomService.register()