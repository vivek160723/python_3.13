# inheritance in Python allows a class (child class) to inherit
# attributes and methods from another class (parent class).
# It helps in code reuse, organization,
# and implementing polymorphism. Here's a breakdown:

# Key Concepts
# Parent Class (Base Class): The class being inherited from.
# Child Class (Derived Class): The class that inherits from the parent class.
#####################################################################################
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return f"{self.name} makes a sound."
#
# # Child class inheriting from Animal
# class Dog(Animal):
#     def speak(self):  # Overriding the speak method
#         return f"{self.name} barks."
#
# # Instantiate objects
# generic_animal = Animal("Some animal")
# dog = Dog("Buddy")
#
# print(generic_animal.speak())  # Output: Some animal makes a sound.
# print(dog.speak())             # Output: Buddy barks.

############################################ single inheritance ###################################################
# class one:
#     def __init__(self):
#         print("i am the parent")
#     def method1(self):
#         print("i am the method of parent class")
#
# class child(one):
#     def __init__(self):
#         print("i am child class")
#     def method2(self):
#         print("hi i am the method of child class")
#
# obj1=child()
# obj1.method1()
# obj1.method2()

############################################ single inheritance ###################################################

# class one1:
#     x,y=10,20
#
#     def m1(self):
#         print(self.x+self.y)
#
# class child2(one1):
#     a,b=100,200
#
#     def m2(self):
#         print(self.a-self.b)
#
#
# obj1=child2()
# obj1.m1()
# obj1.m2()

############################################ Multi-level inheritance ###################################################

# class parent():
#     a,b=10,20
#     def m1(self):
#         print(self.a+self.b)
#
# class child1(parent):
#     x,y=30,40
#     def m2(self):
#         print(self.x+self.y)
#
# class child2(child1):
#     c,d=50,60
#     def m3(self):
#         print(self.c*self.d)
#
# obj3=child2()
# obj3.m1()
# obj3.m2()
# obj3.m3()

############################################ Hierarchy inheritance #################################################

# class parent1():
#     a,b=10,20
#     def m1(self):
#         print(self.a+self.b)
#     def m2(self):
#         print(self.a*self.b)
#
# class child1(parent1):
#     x,y=30,40
#     def m12(self):
#         print(self.x+self.y)
#
# class child2(parent1):
#     x,y=30,40
#     def m3(self):
#         print(self.x+self.y)
#
# obj1=child1()
# obj1.m1()
# obj2=child2()
# obj2.m2()
# # obj2.m12()

############################################ Multiple inheritance ############################################

class parent2():
    a,b=10,20
    def m1(self):
        print(self.a+self.b)

class parent3():
    x,y=30,40
    def m12(self):
        print(self.x+self.y)

class child2(parent2,parent3):
    x,y=30,40
    def m3(self):
        print(self.x+self.y)

obj=child2()
obj.m1()
obj.m12()

