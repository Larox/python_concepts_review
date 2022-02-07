# Dynamic imports

When importing Python packages, we have to consider the namespaces.

`import math`

will be added to the global namespace

`from math import pi`

will add pi to the global namespace

But what if we want to import the module only when it is needed. This is only
possible in runtime. So that's possible with `importlib`.

The `importlib.import_module` will return a module object that can be bind to any
variable. And that variable can be treat as a regularly imported module.

```py
import importlib

module_name = "math"
module = importlib.import_module(module_name)

print(module.__doc__)
```

`import_module` receives the name of the module as argument. And will import the
specific module. The most important difference between the `import` functions and
`import_module` is that `import_module()` returns the specified package or module
(e.g. pkg.mod), while `__import__()` returns the top-level package or module (e.g. pkg).
