from user_services.service_base import ServiceBase


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

