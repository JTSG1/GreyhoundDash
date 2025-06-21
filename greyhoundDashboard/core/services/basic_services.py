from core.services.service_base import ServiceBase, EnhancedServiceBase

class ServiceProxmox(ServiceBase):

    """
    🖥️ < Virtualization!
    """
    id:str = 'proxmox'
    name:str = 'Proxmox'
    description:str = 'An open-source virtualization management platform for running and managing virtual machines and containers using KVM and LXC technologies.',
    tags: list[str] = ['virtualization', 'infrastructure', 'hypervisor', 'containers', 'kvm', 'self-hosted']
    is_enhanced: bool = False

    def get(self) -> ServiceBase:

        super().get()

        return self


class ServiceOpenWebUI(ServiceBase):

    """
    🤖 < AI!
    """
    id:str = 'openwebui'
    name:str = 'Open WebUI'
    description:str = 'A sleek, self-hosted interface for interacting with large language models like ChatGPT, supporting local backends such as Ollama and LM Studio.',
    tags: list[str] = ['AI', 'LLM', 'chatbot', 'self-hosted', 'open-source']
    is_enhanced: bool = False

    def get(self) -> ServiceBase:

        super().get()

        return self