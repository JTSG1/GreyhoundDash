from services.service_base import ServiceBase

class ServiceAnsibleNas(ServiceBase):
    """
    🗃️ Ansible NAS
    """
    id: str = 'ansible_nas'
    name: str = 'Ansible NAS'
    description: str = 'A project for managing network-attached storage (NAS) using Ansible.'
    tags: list[str] = ['ansible', 'nas', 'automation', 'self-hosted', 'open-source']

    def get(self) -> ServiceBase:
        super().get()
        return self
    
    
# Logo URL
# Logo for Ansible NAS can be found at: https://github.com/DaveStephens/ansible-nas/raw/main/assets/logo.png    
