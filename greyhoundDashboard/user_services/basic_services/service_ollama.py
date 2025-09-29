from user_services.service_base import ServiceBase


class ServiceOllama(ServiceBase):
    """
    🦙 Ollama
    """
    id: str = 'ollama'
    name: str = 'Ollama'
    description: str = 'Run large language models locally with ease. Ollama provides a simple interface and support for models like LLaMA, Mistral, and more.'
    tags: list[str] = ['LLM', 'AI', 'local', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
