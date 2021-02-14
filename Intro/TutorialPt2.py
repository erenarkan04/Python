age = 22
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

name = "eren"
if not name:
    print("name is empty")

if age <= 65 and age >= 18:
    print("eligible")

# alternate version
if 18 <= age <= 65:
    print("eligible")

# Ternary operator

print("adult") if age >= 18 else print("not adult")

# Loops

for x in "python":
    print(x)

for x in ["a", "b", "c"]:
    print(x)

for x in range(2, 5):
    print(x)

for x in range(0, 10, 2):
    print(x)

# For...else block - will execute if loop completes without breaking
names = ["john", "eren"]

for name in names:
    if name.startswith('j'):
        print("Found")
        break
else:
    print("Not found")

# While loop
guess = 0
answer = 5


# while guess != answer:
#     guess = int(input("Input: "))


# Functions
def increment(number, by):
    return (number, number + by)


# Can return a tuple (a function returning more than one value)
print(increment(2, by=3))


# using keyword argument to make code more readable

# can also set default values
def increment(number, by=1):
    return (number, number + by)


print(increment(3))


# can pass array of arguments through function

def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(1, 2, 3, 4))

# can also pass objects through function

def save_user (**list):
    print(list)

save_user(id=1, name="Eren")