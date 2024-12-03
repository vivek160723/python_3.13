
# Constructors in python
# its name is fixed def __inti__(self)
# it will not return any value
# can also receive argument and parameter

# ################################ Constructor ######################################
class My_class:
    def __init__(self):
        print("Hi Bad mosh gaurav")

    def gaurav(self):
        print("I am not bad mosh gaurav")
        print(self)

obj1=My_class()
obj1.gaurav()
# ########################### parameterized constructor ############################
class my_class:
    def __init__(self,name,age):
        print(f"hi",name,"you are ",age,"years old.")

obj1=my_class("vivek",23)

# ###################################################################################
class my_class:
    def __init__(self,name,age,sal):
        self.n=name
        self.a=age
        self.s=sal

    def display(self):
        print(self.n,self.a,self.s)

obj11=my_class("vivek",23,2000000)
obj11.display()
####################################################################################
class my_class2:
    def __str__(self):
        return "vivek pro+_player"

obj2=my_class2()
print(obj2)
################################### del keyword #####################################
class my_class:
    def __init__(self,name,age,sal):
        self.n=name
        self.a=age
        self.s=sal

    def display(self):
        print(self.n,self.a,self.s)

obj2=my_class("vivek",23,2000000)
obj2.display()
del obj2.a # here the a attribute is deleted  by using the del keyword
obj2.display()
####################################################################################