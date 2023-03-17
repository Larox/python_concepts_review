# How to distribute a Python package through Pypi

## Important Files for the package

### The setup.py file

This file contains all the meta data from the project including name, version
and the dependencies it needs to work.

```py
from setuptools import setup, find_packages

setup(
    name='the_package_name',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'package_script=the_package_name.__main__:main'
        ]
    }
)
```

### Readme File instructions

This is similar to a project Readme. It must include the project information like:

- version
- CI and tests status
- How to use it

### License file

The license file must include the license terms and conditions, like MIT.

## Creating the package bundle

The package directory must include the `setup.py`, `Readme` and `License` files.

In a directory include the Python Package with all it's code as a Python module.

```
the_package_name/
   module_library.py
   __init__.py
Readme.md
LICENSE
setup.py
```

## Creating the Source Distribution

The source distribution will create a `.tar.gz` file located in `dist/` directory.

The sdist contains the source code of the Python project and all the necessary
files to build and install the package.

`$ python setup.py sdist`

## Creating the Wheel Distribution

The Wheel Distribution will create a `.whl` file in the `dist/` directory.

This distribution is a pre-built package format that contains compiled code and
metadata files. This helps to make the installation of the packages faster and
easier avoiding the compiling step during the installation.

## Creating a Pypi account

Create and account in pypi.org and generate an API token.

## Package uploading

It is recommended to use [Twine](https://pypi.org/project/twine/), a utility for
publishing Python packages on Pypi.

1. Install it using `pip install twine`
2. cd to `dist/` directory
3. Run
   `twine upload --repository the_package_name -u USERNAME -p API_TOKEN dist/*`

Replace the USERNAME with the Pypi username created and API_TOKEN with the token
generated previously.
