class Vehicle:
    def move(self):
        print("its moving")

class Bike(Vehicle):
    def move(self):
        print("Bike is flying")

class Car(Vehicle):
    def move(self):
        print("the car is moving")

ans=[Bike(),Car()]
for i in ans:
    i.move()
