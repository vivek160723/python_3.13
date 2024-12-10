class Parent:
    def __init__(self, name):
        self.name = name
        print(f"{self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"{self.age}")

child_instance = Child("Trivansh", 200)