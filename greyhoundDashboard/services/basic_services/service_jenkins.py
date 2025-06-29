from services.service_base import ServiceBase

class ServiceJenkins(ServiceBase):
    """
    🔧 Jenkins CI/CD
    """
    id: str = 'jenkins'
    name: str = 'Jenkins'
    description: str = 'An open-source automation server that enables developers to build, test, and deploy their software with ease.'
    tags: list[str] = ['CI/CD', 'DevOps', 'automation', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
    