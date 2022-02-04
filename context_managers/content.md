# Context Managers

Context managers allow to allocate and release resources precisely when you need
or want to.

One of the most popular is `with` statement.

```py
# No context manager
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()

# With Context Manager
# Less boilerplate code
with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')
```

1. statement `with` stores the `__with__` method of the `open` class.
2. calls the `__enter__` method of the `open` class.
3. `__enter__` method opens the file and returns it
4. The open file handle is pass to `opened_file`
5. execute the code inside the context manager
6. `with` statement calls `__exit__`
7. `__exit__` method closes the file

To create an own context manager we can leverage using classes and `__exit__`
`__enter__`.

```py
class FileContext:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, expt_type, expt_value, expt_traceback): # exception related values
        self.file_obj.close()
        return True

with FileContext("foo.txt", "w") as open_file:
    open_file.write("bar") # calls write from self.file_obj


class MathContext:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __enter__(self):
        return self
    def __exit__(self, exp_type, exp_val, exp_traceback):
        print(exp_type)
        print(exp_val)
        print(exp_traceback)
        return True

    def do_math(self):
        return a + b

with MathContext(1 + 2) as m:
    m.do_math()
```

Context manager as generator:

```py
from contextlib import contextmanager

@contextmanager
def math_context(a, b):
    math = MathClass(a, b) # assume MathClass exist and has a do_math method
    try:
        yield math
    finally:
        return True

with math_context(1,2) as m:
    m.do_math()
```
