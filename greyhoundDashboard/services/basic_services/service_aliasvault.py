from services.service_base import ServiceBase

class ServiceAliasVault(ServiceBase):
    """
    🔐 AliasVault
    """
    id: str = 'aliasvault'
    name: str = 'AliasVault'
    description: str = 'An end-to-end encrypted password and email alias manager that protects your privacy by creating alternative identities, passwords, and email addresses for every website you use.'
    tags: list[str] = ['password manager', 'email alias', 'privacy', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for AliasVault
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()

    @classmethod
    def is_web_app(cls) -> bool:
        return True

    @classmethod
    def logo(cls) -> str:
        return 'https://www.aliasvault.net/logo.png'

    @classmethod
    def branch_name(cls) -> str:
        return 'main'