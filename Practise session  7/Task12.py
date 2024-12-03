import math


class Circle:
    def __init__(self, radius):
        """Initializes the Circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """Calculates the circumference of the circle."""
        return 2 * math.pi * self.radius


# Main function to interact with the Circle class
def main():
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)

    print(f"\nFor a circle with radius {radius}:")
    print(f"Area: {circle.area():.2f}")
    print(f"Circumference: {circle.circumference():.2f}")


# Running the program
main()
