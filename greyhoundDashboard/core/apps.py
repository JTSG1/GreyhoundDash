from django.apps import AppConfig
import importlib
import inspect
from .services.service_registry import ServiceDefinitions

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):

        module = importlib.import_module("core.services")

        for name, obj in inspect.getmembers(module, inspect.isclass):
            
            if name.startswith("Service") and not name.endswith("Base"):

                obj.register()

        print(ServiceDefinitions)