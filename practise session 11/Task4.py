class Person:
    name="vivek"
    age=23
    def m1(self):
        print(f"{self.name} {self.age}")

class Employee(Person):
    def display(self,id,sal):
        print(id,sal)
        super().m1()



obj1=Employee()
obj1.display(12,10000)