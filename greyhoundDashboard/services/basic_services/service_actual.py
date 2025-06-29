from services.service_base import ServiceBase

class ServiceActual(ServiceBase):
    """
    💰 Actual Budget
    """
    id: str = 'actual'
    name: str = 'Actual Budget'
    description: str = 'A privacy-focused, local-first personal finance app that utilizes the Envelope Budgeting methodology to help users manage their finances effectively.'
    tags: list[str] = ['budgeting', 'personal finance', 'privacy-focused', 'local-first', 'open-source']
    up_check: bool = True

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Assuming the template is located at 'templates/enhanced-services/actual.html'
        template_path = files('greyhoundDashboard.services').joinpath('templates/enhanced-services/actual.html')

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
            is_enhanced=True,
            service_class=cls,
            enhanced_auth_fields=[]
        ))

    def up_check(self):
        # Implementing a simple up check by verifying the availability of the Actual Budget website
        try:
            request = requests.get('https://actualbudget.org', timeout=3)

            if request.status_code == 200:
                return True
            else:
                return False
        except Exception:
            return False

    @classmethod
    def logo(cls) -> str:
        # Assuming the logo is available at 'static/logos/actual.png'
        return '/static/logos/actual.png'

    @classmethod
    def branch_name(cls) -> str:
        return 'main'

    @classmethod
    def web_app(cls) -> bool:
        return True
