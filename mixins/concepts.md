# Mixins

Mixins are a pattern that helps avoid single inheritance (multi level) and
multiple inheritance (diamond dependencies).

A mixin is a class that defines and implements a single, well defined feature.
A subclass can inherit from a mixin, but will inherit only that feature and nothing else.

By convention mixins must end in mixing and follow the class convention of upper-case.

`FooMixin`

Mixins provide a "multiple inheritance" without the issue of having diamond dependencies
