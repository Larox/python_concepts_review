# Module Directory Structure

Modulues in Python are main organization layer available that allows to separate
code into multiple parts, where each of them holds related data and functionality.

This organization helps for import statements to be clear and organized. It is
recommended to keep modules namind short and lowercase and avoid special symbols
since this might cause errors when importing.

When creating a module, and underscores are needed this might lead to the creation
of submodules instead. This helps to the module organization and prevents import
errors:

```py
# Good Practice
import module.plugin.functionality

# Not Recommended
import module.functionality_plugin
```

When working with modules, readibility can be harmed if imports are not properly
handled.

```py
# Not recommeneded since readability will decrease and understanding the code
# will be hard
from module.plugin.functionality import *

some_var = pow(2, 2) # this might be confusing, is this built-in pow or from the import?
```

```py
# readability increases but can lead to confusions if it is redifined in the code
from module.plugin.functionality import pow

some_var = pow(2, 2)
```

```py
# Readable and prevents confusion
import module.plugin.functionality

some_var = functionality.pow(2, 2)
```

```py
# import alias, readable and used as convention by multiple libraries
import numpy as npy
import pandas as pd
```
