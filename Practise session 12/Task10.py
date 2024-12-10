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

if __name__ == "__main__":
    shape = Shape()  # u can not make object of Abstract class
    circle = Circle()
    circle.display()
    circle.draw()