import math

# **Strings**
hello = "hello world"
print(hello)
print("*" * 10)


print(len(hello))
print(hello[0])
print(hello[0: 5])
print(hello[:5])
print(hello[6:])

firstname = "eren"
lastname = "arkan"

# Formatted Strings: whats between curly braces replaced at runtime
full = f"{ firstname} {lastname}"

print(full)

print(full.upper())
print(full.lower())
print(full.title())
print(hello.strip())
print(full.find("a"))
print(full.replace("a", "x"))
print("eren" in full)
print("eren" not in full)

# **Integers**

number = 5
number += 1

print(number / 2)
print(number // 2)
print(number ** 2)
print(number + 2)

# uppercase denotes constants
PI = 3.14
print(round(PI))
print(round(PI))

# convert variable types
# int()
# float()
# bool()
# str()

#
x = input("x: ")
print(int(x) + 2)




