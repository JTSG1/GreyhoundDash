from user_services.service_base import ServiceBase


class ServiceOpenWebUI(ServiceBase):

    """
    🤖 < AI!
    """
    id:str = 'openwebui'
    name:str = 'Open WebUI'
    description:str = 'A sleek, self-hosted interface for interacting with large language models like ChatGPT, supporting local backends such as Ollama and LM Studio.'
    tags: list[str] = ['AI', 'LLM', 'chatbot', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:

        super().get()

        return self