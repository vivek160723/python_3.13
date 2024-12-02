class calculator:
    def add(self,a,b):
        print(a+b)

    @staticmethod
    def display():
        print("This is a calculator:")

obj1=calculator()
calculator.display()
obj1.add(5,5)

