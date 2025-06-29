from services.service_base import ServiceBase

class ServiceGrafana(ServiceBase):
    """
    📊 Grafana
    """
    id: str = 'grafana'
    name: str = 'Grafana'
    description: str = 'An open-source platform for monitoring and observability, offering beautiful dashboards and integrations with Prometheus, Loki, and other data sources.'
    tags: list[str] = ['monitoring', 'dashboards', 'observability', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

