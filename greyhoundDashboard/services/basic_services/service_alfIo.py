from services.service_base import ServiceBase

class ServiceAlfIo(ServiceBase):
    """
    Alf.io is an open-source event attendance management system designed for event organizers who prioritize privacy, security, and fair pricing policies for their customers. 
    It offers a comprehensive suite of tools covering the entire event lifecycle, from ticket distribution to event management and reporting.
    ([facts.dev](https://www.facts.dev/p/alf-io/?utm_source=openai))
    The platform is accessible via web browsers and provides mobile applications for iOS and Android, facilitating attendee check-ins and badge scanning.
    
    Alf.io supports various payment gateways, including Stripe and Mollie, ensuring PCI compliance and secure transactions.
    ([directory.fsf.org](https://directory.fsf.org/wiki/Alf.io?utm_source=openai))
    The user interface is built upon the Twitter Bootstrap framework, ensuring a mobile-first, responsive design.
    ([selfhostedhub.com](https://selfhostedhub.com/project/alf.io?utm_source=openai))
    Alf.io is available in multiple languages, including Italian, English, Spanish, German, Dutch, French, Turkish, Romanian, and Portuguese.
    ([selfhostedhub.com](https://selfhostedhub.com/project/alf.io?utm_source=openai))
    The platform is licensed under the GPL-3.0 license, allowing users to modify and redistribute the software.
    ([github.com](https://github.com/alfio-event/alf.io?utm_source=openai))
    Alf.io is a web application.
    
    
    """
    id: str = 'alfio'
    name: str = 'Alf.io'
    description: str = 'An open-source event attendance management system designed for event organizers who prioritize privacy, security, and fair pricing policies for their customers.'
    tags: list[str] = ['event management', 'ticketing', 'open-source', 'self-hosted', 'privacy', 'security']

    def get(self) -> ServiceBase:
        super().get()
        return self

