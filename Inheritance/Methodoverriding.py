class parent:
    def m1(self):
        print("i am form parent")

class child1(parent):
    def m1(self):
        super().m1()  # if u use super it call all the methods anf dont override
        # super()  evoke immediate parent class methods and variables
        print("i am from child1")


obj=child1()
obj.m1()