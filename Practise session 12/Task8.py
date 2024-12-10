class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

dog = Dog("Sheeru", "Golden Retriever")
cat = Cat("victoria", "German Shephard")

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
