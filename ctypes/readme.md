# Interfacing with External Code: ctypes

`ctypes` provides compatible data types with C language.
It allows calling functions in DLLs (shared libraries).

## How to Import and Use the Library?

These libraries can be loaded dynamically (cdll)

```py
import ctypes

c_library = ctypes.CDLL('path/to/<library>.so')
c_library.<method_name>()
```

## How to Generate .so Files?

`.so` files are shared object library, and are linked to the runtime and if any
change happens in the `.so` file, there is no need to recompile the main program
(library code).

To generate the `.so` file from the `.c` file, use:

```bash
gcc -fPIC -shared -o ./path/output_file_name.so ./path/to/library_in_c_code.c
```

Where:

- `gcc`: GNU compiler collection. Includes C, C++ among others
- `fPIC`: force Position Independent Code. enables the address of shared
  libraries to be relative so that the executable is independent of the position
  of libraries. This enables one to share built library which has dependencies on
  other shared libraries.

- `-o`: output file
- `-shared`: tells the compiler to generate a shared library file instead of an
  executable binary.

- `-o clibrary.so`: specifies the name and location of the output file, which in
  this case is named "clibrary.so" and is placed in the current directory.

- `library_in_c_code.c`: is the name of the C source code file that will be
  compiled into the shared library.

This will compile the source code in the the C file and create a shared library
file (.so) in the specified directory

## Typing the methods

To prevent our ctype method to receive any parameter, we can protect it with
types from C language as an extra layer of coverage.

Importing the library and adding some set up for the types like this:

```py
# Typing and syntax sugar call
c_library = ctypes.CDLL("./so_files/addition.so")

addition = c_library.addition

addition.argtypes = [ctypes.c_int, ctypes.c_int]
addition.restype = ctypes.c_int

print(addition(1, 3))
```

This way, the function is also easier to use. Instead of calling it from the
`c_library`, now it can be called on its own.
