from services.service_base import ServiceBase

class ServiceAcpAdmin(ServiceBase):
    """
    CSA Admin
    """
    id: str = 'acpAdmin'
    name: str = 'CSA Admin'
    description: str = 'A web-based application designed to simplify the management of Community Supported Agriculture (CSA) organizations, offering features like member management, delivery scheduling, automated billing, and more.'
    tags: list[str] = ['CSA management', 'web application', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Assuming the template is located at 'templates/acpAdmin.html'
        template_path = files('services').joinpath('acpAdmin.html')

        if not template_path.exists():
            raise FileNotFoundError(f'Template not found: {template_path}')

        with open(template_path, encoding='utf-8') as fh:
            template_string = fh.read()

        template = Template(template_string)

        return mark_safe(template.render(Context({'state': self.state})))

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

# Register the service
ServiceAcpAdmin.register()