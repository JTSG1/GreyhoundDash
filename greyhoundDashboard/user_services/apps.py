# user_services/apps.py
from django.apps import AppConfig
import importlib, pkgutil, inspect

class UserServicesConfig(AppConfig):
    name = "user_services"

    def ready(self):
        
        import user_services.basic_services as basic_pkg
        import user_services.enhanced_services as enhanced_pkg

        for pkg in (basic_pkg, enhanced_pkg):
            for modinfo in pkgutil.iter_modules(pkg.__path__, prefix=f"{pkg.__name__}."):
                mod = importlib.import_module(modinfo.name)

                for _, obj in inspect.getmembers(mod, inspect.isclass):
                    # Convention: service classes start with "Service"
                    if hasattr(obj, "register") and obj.__name__.startswith("Service"):
                        obj.register()