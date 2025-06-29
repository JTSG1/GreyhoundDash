from services.service_base import ServiceBase

class ServiceAliasVault(ServiceBase):
    """
    🔐 AliasVault
    """
    id: str = 'aliasvault'
    name: str = 'AliasVault'
    description: str = 'AliasVault is a secure platform for managing and protecting sensitive information such as passwords, API keys, and other secrets.'
    tags: list[str] = ['security', 'secrets management', 'passwords', 'API keys']

    def get(self) -> ServiceBase:
        super().get()
        return self
