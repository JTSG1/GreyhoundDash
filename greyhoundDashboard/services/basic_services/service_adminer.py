from services.service_base import ServiceBase

class ServiceAdminer(ServiceBase):
    """
    Adminer
    ([adminer.org](https://www.adminer.org/en/?utm_source=openai))
    """
    id: str = 'adminer'
    name: str = 'Adminer'
    description: str = 'A lightweight, full-featured database management tool written in PHP, supporting various databases including MySQL, PostgreSQL, SQLite, and more.'
    tags: list[str] = ['database management', 'PHP', 'open-source', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Adminer is a PHP-based application; ensure the server supports PHP and has the necessary database extensions installed.
        # Refer to Adminer's official documentation for installation and configuration details.
        return super().render()