
# While loop
number = 100
while number > 1:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO" + command)

while True:
    command = input(">")
    print("ECHO" + command)
    if command.lower() == "quit":
        break

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print("we have " + str(count))

