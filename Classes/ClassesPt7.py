from collections import namedtuple

# for classes with only data (fields) and no methods, it's easier to use a namedtuple

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=3, y=4)

print(p1 == p2)