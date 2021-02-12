numbers = [5, 6, 34, 7, 9]

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)

print(sorted(numbers))
print(sorted(numbers, reverse=True))


items = [("a", 3), ("b", 6), ("c", 1)]

def sort (item):
    return item[1]

# items.sort(key=sort)

# same thing using lambda expression (temporary function to pass through the sort function
items.sort(key= lambda item: item[1])

print(items)

# Map function

prices = list(map(lambda item:item[1], items))
print(prices)

# Filter function
filtered_prices = list(filter(lambda item: item[1] >= 3, items))
print(filtered_prices)

# Iterator comprehension - same result as map function
prices2 = [item[1] for item in items]
print(prices2)
xxx
prices3 = [item for item in items if item[1] >= 3]
print(prices3)

# Zip function
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list(zip(list1, list2)))

# Stack
# with browser back button logic

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session.pop())
if not browsing_session:
    print("exit")
