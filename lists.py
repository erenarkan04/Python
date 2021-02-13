letters = ["a", "b", "c"]

matrix = [[1,2], [3,4]]

zeros = [0] * 5

combined = zeros + letters

print(combined)

# can use list() command to convert any iterable to a list

list1 = list(range(1,20))

print(list1)

print(list("Hello world"))

print(list1.__len__())
print(len(list1))

print(letters[0:2])

# Can also add a step to get every nth item in the list
print(letters[::2])
print(letters[::-1])

# List unpacking
first, second, third = letters
print(first)
print(second)
print(third)

# can pack the rest of the elements into *others if not needed
a, b, *others = letters

# enumerate gives tuple with the index and value of each item in the list
for letter in enumerate(letters):
    print(letter)

# can also unpack what you enumerate previously to show like this. Can use to get the index while iterating a string
for index, letter in enumerate(letters):
    print(index, letter)

# use .append to add, .insert to add in the middle or beginning
letters.append("d")
letters.append("e")
letters.append("f")
letters.insert(0, "d")
letters.remove("b")
letters.pop()
letters.pop(2)
# letters.clear() to clear the whole list

print(letters)

del letters[0:2]

print(letters)

if "e" in letters:
    (letters.index("e"))

letters.append("d")
letters.append("d")

print(letters.count("d"))