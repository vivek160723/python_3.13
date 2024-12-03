class car:
    def __init__(self,name,age):
        self.age=age
        self.name=name
        print(name,age)

obj1=car("vivek",23)
del obj1.age
print(obj1.age)




