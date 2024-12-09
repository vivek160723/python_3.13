class Animal:
    def sound(self):
        print("sabki apni marjji")

class dog(Animal):
    def sound(self):
        print("bhauu bhauu")

class cat(Animal):
    def sound(self):
        print("meoww")

class cow(Animal):
    def sound(self):
        print("mooooooowwwww")

obj1=dog()
obj1.sound()
obj2=cat()
obj2.sound()
obj3=cow()
obj3.sound()