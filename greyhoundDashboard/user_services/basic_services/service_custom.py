from user_services.service_base import ServiceBase


class ServiceCustom(ServiceBase):

    """
    Custom!
    """
    id:str = 'custom'
    name:str = 'Custom'
    description:str = 'To be used for custom services that do not fit into the other definitions.'
    tags: list[str] = ['custom']

    def get(self) -> ServiceBase:

        super().get()

        return self

