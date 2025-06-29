from services.service_base import ServiceBase

class ServiceAkkoma(ServiceBase):
    """
    🐦 Akkoma
    """
    id: str = 'akkoma'
    name: str = 'Akkoma'
    description: str = 'Akkoma is a fork of Mastodon focused on providing a lightweight social media experience.'
    tags: list[str] = ['social', 'activitypub', 'self-hosted']

    def get(self) -> ServiceBase:
        super().get()
        return self

