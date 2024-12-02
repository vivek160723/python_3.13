class Car:
    name=""
    brand=""
    def car_info(self,name,brand):
        print(f"Name =",name,"Brand =",brand)

obj1=Car()
obj2=Car()
obj3=Car()

obj1.car_info("i20","Hyundai")
obj2.car_info("Baleno","Suzuki")
obj3.car_info("Swift","Suzuki")