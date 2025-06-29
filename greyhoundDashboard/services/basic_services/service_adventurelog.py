from services.service_base import ServiceBase

class ServiceAdventureLog(ServiceBase):
    """
    🌍 AdventureLog
    """
    id: str = 'adventurelog'
    name: str = 'AdventureLog'
    description: str = 'An open-source, self-hosted travel tracker and trip planner designed to help you manage your journeys with ease.'
    tags: list[str] = ['travel', 'tracker', 'trip planner', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Assuming the template is located at 'services/adventurelog/templates/adventurelog.html'
        template_path = files('services.adventurelog').joinpath('templates', 'adventurelog.html')

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
            enhanced_auth_fields=cls.enhanced_auth_fields
        ))
