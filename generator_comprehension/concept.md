# Generators Comprehension

Generators are an special type of iterator that generates the value on the fly
by storing the instruction of how to generate the value instead of storing the
value.

`range` is a generator

## Creating a generator comprehensions

### Syntax

The expresion to produce a generator comprehension is the following:

```
(<expression> for <var> in <iterable> if <condition>)
```

This produce a generator, where the instructions for generating its members are
provided inside the parenthesis.

```py
own_generator = (i for i in range(100) if i%5) # 5 - 10 - 15

# Equivalent to
for i in range(100):
    yield i
```

Generator comprehensions can include other structures like tuples:

```py
((i, i*2, i*3) for i in range(5))

# (0, 0, 0)
# (1, 2, 3)
# (2, 4, 6)
# ...
```
