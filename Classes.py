class Point:

    default_color = "red "
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0,0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"point({self.x}, {self.y})")



point = Point(1, 2)
other = Point(1, 2)
point_zero = Point.zero()
point.draw()
point_zero.draw()
print(point)
print(point == other)
total = point + other
print(total)