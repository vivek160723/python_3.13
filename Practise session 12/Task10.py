from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    def display(self):
        print("This is a shape.")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")

circle = Circle()
circle.display()
circle.draw()