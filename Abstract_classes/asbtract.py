from abc import ABC, abstractmethod


class parent(ABC):
    @abstractmethod
    def display(self):
        pass
class child(parent):
    def display(self):
        print("HI i am noone")

    @abstractmethod
    def c1(self):
        pass
class child2(child):
    def c1(self):
        print("i am child2")

obj1=child2()
obj1.display()
obj1.c1()