class Product:
    def __init__(self, price):
        self.price = price

    # making getter/setter for the object with built in logic to prevent < 0 input and making it into a property
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("price cannot be < 0")
        self.__price = price


# Inheritance - Animal is the base/parent class and Mamal and Fish are the base class

class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

class Mamal(Animal):

    # .super() refers to the parent class to call it's constructor inside the constructor of the child class

    def __init__(self):
        super().__init__()
        self.weight = 1

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")

m = Mamal()
print(isinstance(m, Mamal))
print(issubclass(Mamal, Animal))