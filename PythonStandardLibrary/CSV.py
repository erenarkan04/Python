import csv

# open in write mode to write data to the file with "w"

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction id", "product id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([25, 3, 123])
    csv.writer(file).writerow([1, 2, 3])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)


