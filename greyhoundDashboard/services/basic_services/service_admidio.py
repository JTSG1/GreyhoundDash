from services.service_base import ServiceBase

class ServiceAdmidio(ServiceBase):
    """
    Admidio
    """
    id: str = 'admidio'
    name: str = 'Admidio'
    description: str = 'A free open-source membership management system optimized for associations, groups, and organizations, offering features like member management, event planning, and document sharing.'
    tags: list[str] = ['membership management', 'open-source', 'associations', 'groups', 'organizations']

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

    def __init__(self, registered_service):
        self.state = {}
        self.registered_service = registered_service
        self.state['up'] = self.up_check()
        self.state['is_enhanced'] = self.is_enhanced
        self.state['enhanced_auth_fields'] = self.enhanced_auth_fields
        self.state['description'] = self.description
        self.state['tags'] = self.tags
        self.state['name'] = self.name
        self.state['id'] = self.id
        self.state['logo'] = self.logo
        self.state['branch_name'] = self.branch_name
        self.state['web_app'] = self.web_app

    is_enhanced: bool = True
    enhanced_auth_fields: list[str] = []
    logo: str = 'admidio_logo.png'
    branch_name: str = 'main'
    web_app: bool = True