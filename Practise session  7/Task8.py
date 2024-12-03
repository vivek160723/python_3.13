class Employee:
    def __init__(self,name,age,sal):
        self.n=name
        self.a=age
        self.s=sal

    def __str__(self):
        return(f"{self.n},{self.a},{self.s}")

obj2=Employee("vivek",23,9000000000000000)
print(obj2)