class Employee:
    name = "vivek"
    sal = 10000

    def update(self, sal, increment):
        self.sal = sal + increment
        return self.sal

    def display(self):
        print(f"Updated Salary: {self.sal}")

obj1 = Employee()
obj1.update(obj1.sal, 500)
obj1.display()
