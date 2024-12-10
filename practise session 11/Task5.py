class Animal:
    def sound(self):
        print("sabki apni marjji")

class dog(Animal):
    def sound(self):
        print("bhauu bhauu")

class cat(Animal):
    def sound(self):
        print("meoww")

ans=[dog(),cat()]
for i in ans:
    i.sound()