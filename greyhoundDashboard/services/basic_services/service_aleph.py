from services.service_base import ServiceBase

class ServiceAleph(ServiceBase):
    """
    Aleph is a data platform developed by the Organized Crime and Corruption Reporting Project (OCCRP) to assist investigative journalists in tracking people and companies, primarily for corruption investigations. ([docs.aleph.occrp.org](https://docs.aleph.occrp.org/about/?utm_source=openai))
    """
    id: str = 'aleph'
    name: str = 'Aleph'
    description: str = 'A data platform developed by OCCRP to assist investigative journalists in tracking people and companies, primarily for corruption investigations.'
    tags: list[str] = ['investigative journalism', 'data analysis', 'open-source', 'corruption investigations']

    def get(self) -> ServiceBase:
        super().get()
        return self

    def render(self) -> str:
        # Aleph is a web-based application accessible at https://aleph.occrp.org/. 
        return super().render()

    @classmethod
    def register(cls) -> None:
        super().register()
