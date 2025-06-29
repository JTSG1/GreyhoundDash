from greyhoundDashboard.services.service_base import ServiceBase


class ActivityWatchService(ServiceBase):
    id = 'activitywatch'
    name = 'ActivityWatch'
    description = 'An open-source time-tracking tool that helps you understand how you spend your time.'
    tags = ['tracking', 'productivity', 'activity']
    up_check = True

    def __init__(self, registered_service):
        super().__init__(registered_service)
        self.enhanced_auth_fields = ['api_key']  # Example of enhanced auth field

    def custom_method(self):
        # You can add custom methods specific to ActivityWatch here
        pass


# Registration of the service
ActivityWatchService.register()