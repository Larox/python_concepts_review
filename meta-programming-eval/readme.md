# What is metaprogramming in Python?

- Everything is Python is an Object
- Classes are an Object
- Classes are created by a metaclass
- Metaclass allow to add special behaviours to a class

- A class is an instance of type, type

```py
class MyFirstMetaClass:
    pass

print(type(myFirstMetaClass)) # <class 'type'>
```

- Type is a metaclass used to creater other classes. Ex:

```py
class MyFirstMetaClass:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return f"Text: {self.text}"

# using type class
def MyFirstMetaClass_init(self, text):
    self.text = text

meta_class = type(
                    "MyFirstMetaClass", # class name
                    (), # tuple of base classes
                    { # dictionary with attributes and implementation {k: v}
                        "__init__": MyFirstMetaClass_init,
                        "get_text": lambda self: f"Text: {self.text}"
                    }
                )
```

Since there is an object, that is why `__dict__` property is part
of all of our objects.

Internally, `__dict__` is use along with descriptors `__set__` `__get__` like:
`__dict__.__get__` or `__dict__.__set__`.

Now, functions are descriptors and can be added to classes at the run time.

To achieve this, meta-class can be used.

# Metaprogramming - How?

1. Create a metaclass

- class that inherits type

```py
class MyMetaClass(type): # Metaclass is defined by inheriting from type
```

- Use the `type.__new__` method that is now available

```py
class MyMetaClass(type): # Metaclass is defined by inheriting from type
    def __new__(cls, class_name, bases=None, dict=None):
        return type.__new__(cls, what=class_name, bases=bases, dict=dict)
```

- Now the metaclass has access to the class name, parents (if inherits from other
  class) and all the attributes

## Disadvantages

- Unexpected side effects if implemented/understood incorrectly.
- It is never the 1st path to follow. Use it when it is the only option to solve
  the needs.

# The `eval` method

`eval` parses the expression passed and run it as Python code within
the program.

the `eval` parameters:

```py
eval(expression: Str, globals: dict, locals: dict)
```

It returns the result of the evaluated expression.

```py
n = 10

eval('list(range(n))') # [0,1,2,3,4,5,6,7,8,9]
```

## Warnings and What to take into account when using `eval`

Since `eval` will run the expression as part of the program, it can have
access to different libraries or modules such as `os` that allows on how to use the operating system functionalities.

This can be spoiled as a security breach where malicious scripts can be executed.

```py
script = input("Type a command") # os.system('rm -rf *')

eval(script) # deletes every file and folder
```

### Restrict locals and globals parameters

When passing specific globals but no local parameters, it will use globals for both local and global variables.

```py
# No Restricted globals or locals
from itertools import chain

foo = ['ABC', 'DEF']

eval('dir()') # will include chain from itertools and foo (local)
eval('list(chain.from_iterable(foo))') # ['A', 'B', 'C', 'D', 'E', 'F']
```

```py
# Restricted globals

from itertools import chain

foo = ['ABC', 'DEF']

eval('dir()', {}) # empty globals, and locals. Won't show chain or foo

# Global restricted
eval('list(chain.from_iterable(foo))', {}) # Will throw error. "chain is not defined"

eval('list(chain.from_iterable(foo))',{"chain": chain}) # Will throw error. "foo is not defined" since "chain" is include in global namespace


eval('list(chain.from_iterable(foo))',{"chain": chain}, {"foo": foo}) # this will output the expected result since chain and foo have been passed as globals and locals.

# eval can use custom names in globals and locals

eval('list(it_chain.from_iterable(iterable_list))',{"it_chain": chain}, {"iterable_list": foo})
```

The `globals` parameters can restrict `__builtins__` module with `{"__builtins__": None}`
