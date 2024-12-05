class laptop:
    brand=""
    model=""
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def specifications(self):
        print(f"{self.brand} {self.model}")

obj1=laptop("Asus","vivobook")
obj2=laptop("apple","Macbook")
obj1.specifications()
obj2.specifications()