# Try block - execute commands in the try block, if exception is encountered execute except block, if not excecute else block
try:
    file = open("Exceptions.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("invalid input")
else:
    print("No exceptions were thrown")
finally:
    file.close()

# finally block excecutes no matter if an exception is thrown, commonly used to close files/database connections

# can also use a with clause to automatically close files/database connections by automatically calling the .__exit method
try:
    with open("Exceptions.py") as file, open("FizzBuzz.py") as target:
        print("file opened")
except (ValueError, ZeroDivisionError):
    print("invalid input")
else:
    print("No exceptions were thrown")


# How to throw exceptions
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be < 0")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError() as error:
    print(error)