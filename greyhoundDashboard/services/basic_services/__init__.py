from . import *
from services.service_base import ServiceBase, EnhancedServiceBase

class ServiceProxmox(ServiceBase):

    """
    🖥️ < Virtualization!
    """
    id:str = 'proxmox'
    name:str = 'Proxmox'
    description:str = 'An open-source virtualization management platform for running and managing virtual machines and containers using KVM and LXC technologies.'
    tags: list[str] = ['virtualization', 'infrastructure', 'hypervisor', 'containers', 'kvm', 'self-hosted']

    def get(self) -> ServiceBase:

        super().get()

        return self


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
    

class ServiceJenkins(ServiceBase):
    """
    🔧 Jenkins CI/CD
    """
    id: str = 'jenkins'
    name: str = 'Jenkins'
    description: str = 'An open-source automation server that enables developers to build, test, and deploy their software with ease.'
    tags: list[str] = ['CI/CD', 'DevOps', 'automation', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
    

class ServiceGrafana(ServiceBase):
    """
    📊 Grafana
    """
    id: str = 'grafana'
    name: str = 'Grafana'
    description: str = 'An open-source platform for monitoring and observability, offering beautiful dashboards and integrations with Prometheus, Loki, and other data sources.'
    tags: list[str] = ['monitoring', 'dashboards', 'observability', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self


class ServicePihole(ServiceBase):
    """
    🛡️ Pi-hole
    """
    id: str = 'pihole'
    name: str = 'Pi-hole'
    description: str = 'A network-wide ad blocker that acts as a DNS sinkhole to block ads, trackers, and malicious domains for all devices on your network.'
    tags: list[str] = ['network', 'ad-blocking', 'dns', 'privacy', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self


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


__all__ = [
    name for name, obj in globals().items()
    if name.startswith('Service') and isinstance(obj, type)
]