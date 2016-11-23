class Animal():
    def __init__(self, color, name, weight):
        self.color = color
        self.name = name
        self.weight = weight

    def __str__(self):
        return self.name + "is also an animal. it's color is " + self.color + " and weights " + str(self.weight) + "kg"

class Cat(Animal):
    def talk(self):
        return "meow"

    def __str__(self):
        return "" + self.name + " is a cat." +super().__str__()



class Dog(Animal):
    def talk(self):
        return "bark"

    def __str__(self):
        return "" + self.name + " is dog." + super().__str__()


class Bird(Animal):
    def talk(self):
        return "chirp"

    def __str__(self):
        return "" + self.name + " is a cat." +super.__str__(super)

animals = [
    Cat("yellow", "kitty", 5),
    Dog("brown", "bob", 6)
]
for animal in animals:
    print(animal)
    print(animal.talk())

