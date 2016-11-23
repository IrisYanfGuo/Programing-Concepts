import math


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getXYloc(self):
        return [self.x, self.y]

    def setXYLoc(self, xvalue, yvalue):
        self.x = xvalue
        self.y = yvalue


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calArea(self):
        return math.pi * self.radius * self.radius


class Square(Shape):
    def __init__(self, x):
        self.width = x

    def calArea(self):
        return self.width * self.width


class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.s1= side1
        self.s2 = side2
        self.s3 = side3

    def calArea(self):
        s = (self.s1+self.s2+self.s3)/2
        return math.sqrt(s*(s-self.s2)*(s-self.s3))

    

