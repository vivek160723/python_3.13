class Book:
    def __init__(self,name,author):
        self.n=name
        self.a=author

    def __str__(self):
        return(f"Book name:{self.n},Author{self.a}")

obj1=Book("Noob+Katha"," sheikh-Gaurav-piere")
print(obj1)