# Debugging with pdb & ipdb

## pdb

pdb is Python's built-in debugger, this helps to check the state of any variable
in the application.

To set a break point and open pdb prompt:

```py
import pdb; pdb.set_trace()  # Since Python 3.7 use breakpoint()

> # shows file information and line where code stopped
-> # Current line where Python paused
```

Useful Commands:

```
Any Python expression can be used in pdb prompt

l: list the current code (11 lines)
ll: long list to print the function where the break point is set source code.
p: print
pp: pretty print
n: continue execution until next line
s: executes current line and stops
b: set a break point. Can use line number, function. No args, list break points
cl: clear break points
u: "up" moves up in the stack trace
```

## ipdb

Interactive Python debugger provides extra features like tab completition,
syntax highlight, better traceback and instrospections. All of this with the same
interface of pdb. It needs to be installed as an external package.
