* [^ Contents](../README.md)

<!-- TOC -->
* [Modules](#modules)
  * [Module reload, importlib](#module-reload-importlib)
<!-- TOC -->

# Modules

## Module reload, importlib

Reload a previously imported module. The argument must be a module object, so it must have been successfully imported
before. This is useful if you have edited the module source file using an external editor and want to try out the new
version without leaving the Python interpreter. The return value is the module object (which can be different if
re-importing causes a different object to be placed in sys.modules).

```python
from importlib import reload  # Python 3.4+
import foo

while True:
    # Do some things.
    if is_changed(foo):
        foo = reload(foo)
```
