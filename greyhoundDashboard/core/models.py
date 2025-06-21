from django.db import models
from core.services.service_registry import ServiceDefinitions

class RegisteredService(models.Model):

    name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50, choices=ServiceDefinitions.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_fields = models.JSONField(default=dict, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Ensure that the service_type is valid
        if self.service_type not in dict(ServiceDefinitions.definition_dict):
            raise ValueError(f"Invalid service type: {self.service_type}")
        
        # set auth_fields based on service_type
        self.process_enhanced_auth_fields()
        super().save(*args, **kwargs)

    def process_enhanced_auth_fields(self):
        if not self.auth_fields:
            auth_fields_list = ServiceDefinitions.definition_dict[self.service_type].enhanced_auth_fields \
                if ServiceDefinitions.definition_dict[self.service_type].enhanced_auth_fields else {}
            self.auth_fields = {field: '' for field in auth_fields_list}
        elif self.auth_fields and not isinstance(self.auth_fields, dict):
            raise ValueError("auth_fields must be a dictionary.")
