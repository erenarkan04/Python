import random
import string

print(random.random())
print(random.randint(1, 20))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5], k=2))

# generate random PW

print("".join(random.choices(string.ascii_lowercase + string.digits, k=8)))

# shuffle

numbers = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(numbers)

print(numbers)