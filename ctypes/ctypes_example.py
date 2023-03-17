import ctypes


# Promt from C code
hello_world = ctypes.CDLL("./so_files/hello_world.so")

hello_world.prompt() # print "Hello World"


# Typing and syntax sugar call
c_library = ctypes.CDLL("./so_files/addition.so")

addition = c_library.addition

addition.argtypes = [ctypes.c_int, ctypes.c_int]

addition.restype = ctypes.c_int

print(addition(1, 3))
