from services.service_base import ServiceBase

class ServiceAirTrail(ServiceBase):
    """
    🌐 AirTrail
    """
    id: str = 'airtrail'
    name: str = 'AirTrail'
    description: str = 'A modern, open-source personal flight tracking system that allows users to track flights, view flight history, and gain insights into their travel patterns.'
    tags: list[str] = ['flight tracking', 'open-source', 'self-hosted', 'web application']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def up_check(self):
        try:
            request = requests.get(self.registered_service.url, timeout=3)
            if request.status_code in [200, 401, 403]:
                return True
            else:
                return False
        except Exception as e:
            return False

    def render(self) -> str:
        template_path = files(".".join(self.__module__.split('.')[0:2])).joinpath(
            f"{self.id}.html"
        )

        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, encoding="utf-8") as fh:
            template_string = fh.read()

        template = Template(template_string)

        return mark_safe(template.render(Context({"state": self.state})))

    @classmethod
    def register(cls) -> None:
        from core.services.service_registry import ServiceDefinitions, ServiceDefinition

        ServiceDefinitions.register(cls.id, ServiceDefinition(
            name=cls.name,
            description=cls.description,
            tags=cls.tags,
            is_enhanced=cls.is_enhanced,
            service_class=cls,
            enhanced_auth_fields=[]
        ))
