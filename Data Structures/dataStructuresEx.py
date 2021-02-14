from pprint import pprint

sentence = "this is a common interview question"

unique_letters = []

for z in sentence:
    if not unique_letters.__contains__(z) and not z == " ":
        unique_letters.append(z)

print(unique_letters)
values = {}
for x in unique_letters:
    count = 0
    for y in sentence:
        if y == x:
            count += 1
    values[x] = count

pprint(values, width=2)

# .items() return the key-value pairs of each item in the dictionary
sorted_values = sorted(values.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_values[0])
