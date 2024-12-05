class car:
    def __init__(self, make, model, year):
        self.m = make
        self.mo = model
        self.y = year
        print(make,model,year)
    def start_engine(self):
        print("Engine is stating.")

obj1=car("Hyundai","i-20",2019)
obj1.start_engine()


