import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("The area method must be implemented by a subclass.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Demonstration
shapes = [
    Rectangle(5, 10),
    Circle(7)
]

for shape in shapes:
    print(f"{shape.area():.2f}")
