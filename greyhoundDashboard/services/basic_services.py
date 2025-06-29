import importlib
import pkgutil

__all__ = []

for modinfo in pkgutil.walk_packages(__path__, prefix=f"{__name__}."):
    mod = importlib.import_module(modinfo.name)
    for name, obj in vars(mod).items():
        if name.startswith("Service") and isinstance(obj, type):
            globals()[name] = obj       # expose it at package level
            __all__.append(name)        # re-export it