class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self,name,age):
        print(f"{name} {age}")

obj1=Person("vivek",23)
obj1.display("rahul",34)
obj1.display("Gaurav",34)

