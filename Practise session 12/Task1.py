# Base class
class Animal:
    pass

# Derived class 1
class Mammal(Animal):
    pass

# Derived class 2
class Bird(Animal):
    pass

# Derived class 3
class Dog(Mammal):
    pass

# Test the issubclass() function
print("Is Mammal a subclass of Animal?", issubclass(Mammal, Animal))  # True
print("Is Bird a subclass of Animal?", issubclass(Bird, Animal))      # True

