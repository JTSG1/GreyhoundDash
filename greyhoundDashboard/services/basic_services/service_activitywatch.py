from greyhoundDashboard.services.service_base import ServiceBase

class ActivityWatch(ServiceBase):
    id = 'activitywatch'
    name = 'ActivityWatch'
    description = 'An open-source time tracking tool.'
    tags = ['tracking', 'activity', 'open-source']
    up_check_timeout = 5  # seconds

    def up_check(self):
        try:
            request = requests.get(self.registered_service.url, timeout=self.up_check_timeout)
            return request.status_code == 200
        except requests.RequestException:
            return False

    @classmethod
    def register(cls) -> None:
        super().register()