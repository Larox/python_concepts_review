# Equality reference logic operator "=="
# Equality checks for the value of the values being checked

# Identity references logic operator "is"
# Identity checks the reference of the values. If both refer to the same object in memory

# This can also be reviewed as checked by reference and checked by value.


print("numbers examples")

num_a = 200
num_b = num_a
num_a = num_b

print(f"num_a id: {id(num_a)}") # will share the object id
print(f"num_b id: {id(num_b)}")

print(f"num_a == num_b (check by value - equality): {num_a == num_b}") # true expected
print(f"num_a is num_b (check by reference - identity): {num_a is num_b}") # true expected

print("\n")

print(" --- list examples")

list_a = [1,2,3]
list_b = [1,2,3]
print(f"list_a id: {id(list_a)}") # won't share the object id
print(f"list_b id: {id(list_b)}")
print(f"list_a == list_b (check by value - equality): {list_a == list_b}") # true expected
print(f"list_a is list_b (check by reference - identity): {list_a is list_b}") # false expected

print("\n")

print("assigning list_b = list_a to share the same object id")

list_b = list_a 
print(f"list_a id: {id(list_a)}") # will share the object id
print(f"list_b id: {id(list_b)}")

print(f"list_a == list_b (check by value - equelity): {list_a == list_b}") # expect true
print(f"list_a is list_b (check by reference - identity): {list_a is list_b}") # expect true

# In Python some values like booleans (True, False, None) reference the same
# object in memory, so "is" operator is recommended. For other cases it is
# recommended to use "==" operator