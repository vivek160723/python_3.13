class Employee:
    def __init__(self,x,y,z):
        self.id=x
        self.name=y
        self.sal=z

    def increment(self,increment):
        self.sal += self.sal + (increment/100)

    def display(self):
        print(f"{self.id} {self.name} {self.sal}")
obj1=Employee(23,"vivek",100000)
obj1.increment(20)
obj1.display()

