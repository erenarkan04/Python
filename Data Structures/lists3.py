from collections import deque
from array import array

# Queues
queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()

# Tuples
list = [1, 2, 3]
tuple(list)

print(type(list))

# Swapping variables
x = 1
y = 2

x, y = y, x

print(x)
print(y)

# Arrays - need to specify typecode "i" = integer
numbers = array("i", [1, 2, 3])

# Sets - can't have duplicate values, defined by {}
unique = set([1, 1, 2, 3])
second = {1, 4, 5}

print(unique | second)

# Print only shared elements in two sets
print(unique & second)

# Print only unique items in first set that dont exist in the second set
print(unique - second)

# Print only items not in both sets
print(unique ^ second)

# Dictionary - similar to hashtable

point = dict(x=1, y=2)
print(point)
print(point["x"])
print(point.get("a", "Null"))
del point["x"]

# loop variable takes the value of the key in each iteration
for key in point:
    print(key, point[key])

# Comprehension
list = []
for x in range(5):
    list.append(x * 2)

# alternate way with comprehension

values = [x * 2 for x in range(5)]

print(values)

# can also use comprehension to create dictionary objects
dictionary = {x : x * 2 for x in range(5)}
print(dictionary)

# Generator objects - can create one by using () with comprehension expressions

values = (x * 2 for x in range(5))
for x in values:
    print(x)

# Unpacking operator

nums = [1, 2, 3]
print(nums)

# Unpacks the list and passes  each item as a separate argument to the print function
print(*nums)

# values1 = list(range(5))
values2 = [*range(5)]
# print(values1)
print(values2)

list1 = [1, 2]
list2 = [3, 4]

print([*list1, *list2])

dict1 = {"x": 10, "y":20}
dict2 = {"z": 15, "u":25}
print({**dict1, **dict2})

