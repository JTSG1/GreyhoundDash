from services.service_base import ServiceBase

class ServiceAnswer(ServiceBase):
    """
    📜 Answer
    """
    id: str = 'answer'
    name: str = 'Answer'
    description: str = 'Answer is a service providing insights and responses from a variety of data sources to help users understand complex datasets in an intuitive way.'
    tags: list[str] = ['data', 'insights', 'analytics']

    def get(self) -> ServiceBase:
        super().get()
        return self
