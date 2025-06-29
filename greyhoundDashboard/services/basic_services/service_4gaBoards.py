from services.service_base import ServiceBase

class Service4gaBoards(ServiceBase):
    """
    4ga Boards
    """
    id: str = '4gaboards'
    name: str = '4ga Boards'
    description: str = 'A straightforward, real-time project management tool designed to boost productivity and provide clear project overviews.'
    tags: list[str] = ['project management', 'task tracking', 'collaboration', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Custom rendering logic for 4ga Boards can be added here
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()

    @classmethod
    def is_web_app(cls) -> bool:
        return True
