from services.service_base import ServiceBase

class ServiceAdminer(ServiceBase):
    """
    Adminer
    ([adminer.org](https://www.adminer.org/en/?utm_source=openai))
    """
    id: str = 'adminer'
    name: str = 'Adminer'
    description: str = 'A lightweight database management tool available for MySQL, MariaDB, PostgreSQL, SQLite, MS SQL, Oracle, and more.'
    tags: list[str] = ['database', 'management', 'webapp', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Adminer is a web-based application, so we can render it directly.
        return super().render()