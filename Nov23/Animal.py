# ppt 40
class Animal(object):
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def talk(self):
        return "Meowl"


# here dog is not the subclaff of animal, but polymorphism can still work. that's different from java and c++
class Dog(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        return "woof woof"


animals = [
    Cat("cat"),
    Dog("dog")
]

for animal in animals:
    print(animal.name + ":", animal.talk())


class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "(%f,%f)" % (self._x, self._y)

    def __add__(self, other):  # overwrite the method other
        return Point(self._x + other._x, self._y + other._y)


class Point1(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "(%s,%s)" % (self._x, self._y)

    def __add__(self, other):  # overwrite the method other
        return Point1(self._x + other._x, self._y + other._y)


c = Point(1, 2)
d = Point(6, 7)
e = c + d
print(c + d)


# ppt45
def foo(point):
    point._x = 100
    return point


def foo1(point):
    point = Point(100, 100)
    return point


print(foo(c))
print(c)
print(foo1(c))
print(c)

from re import *

b=match('[a-z]+',"5adsf22")
print(b)