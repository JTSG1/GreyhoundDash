# module/__init__.py
"""
Expose every class defined in any sub-module whose name ends with *Service*
(or pick whatever rule you need) so callers can simply::

    from module import MyService
"""
import pkgutil
import importlib
import inspect

__all__: list[str] = []          # what `from module import *` will export
_pkg_name = __name__             # e.g. "module"

for modinfo in pkgutil.walk_packages(__path__, prefix=f"{_pkg_name}."):
    # 1. import the sub-module (e.g. module.service_test)
    mod = importlib.import_module(modinfo.name)

    # 2. promote matching classes to the package namespace
    for name, obj in vars(mod).items():
        if inspect.isclass(obj) and name.startswith("Service"):
            globals()[name] = obj   # expose at package level
            __all__.append(name)    # re-export
