
# Imperative way of removing dots in a string
from dataclasses import dataclass
from os import remove
from typing import Callable


def remove_dots_in_string(u_string: str) -> str:
    """
    Multiple statements that carry out actions needed to have a string with no
    dot in it. In this case return the string with no dots.
    """
    split_string = u_string.split(".")
    new_string = "".join(split_string)
    return new_string


# Declarative way of removing dots in a string
# In this case, we just have an action to perform the dots removal, and will
# determine a value, in this case the string with no dots.
# It can be reused as the previous one since it is not binded to a name, unless
# it is assigned to a variable, but this would break the lambda concept.
lambda u_string : u_string.replace(".", "")


u_string = "this.has.multiple.dots"

remove_dots_in_string(u_string)# thishasmultipledots


@dataclass
class StringUtils:
    u_string: str
    dot_removal: Callable[[str], str]

    def perform(self) -> str:
        return self.dot_removal(self.u_string)

# in this case, we are using a lambda expression injecting the dependency instead
# of relying in an implementation/dependency inside the class
# and making the class easier to test :D 
str_utils = StringUtils(u_string, lambda u_string : u_string.replace(".", ""))

str_utils.perform() # thishasmultipledots
