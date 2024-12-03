class Employee:
    name = "vivek"
    sal = 100000

    def update(self, sal, increment):
        self.sal = sal + increment
        return self.sal

    def display(self):
        print(f"Updated Salary: {self.sal}")

obj1 = Employee()
obj1.update(obj1.sal, 5000)
obj1.display()
