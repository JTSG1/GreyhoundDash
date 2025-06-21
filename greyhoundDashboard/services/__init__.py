import importlib
import pkgutil

# Get the current package name
__all__ = []

for loader, module_name, is_pkg in pkgutil.iter_modules(__path__):
    # Dynamically import submodules
    full_module_name = f"{__name__}.{module_name}"
    module = importlib.import_module(full_module_name)

    # Optionally bring their symbols into the top-level namespace
    if hasattr(module, '__all__'):
        globals().update({k: getattr(module, k) for k in module.__all__})
        __all__.extend(module.__all__)
    else:
        # Just expose the module itself if __all__ not defined
        globals()[module_name] = module
        __all__.append(module_name)
