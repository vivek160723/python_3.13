# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
#
#     def display(self):
#         print("This is a shape.")
#
# class Circle(Shape):
#     def draw(self):
#         print("Drawing a circle.")
#
# shape = Shape()  # u can not make object of Abstract class
# circle = Circle()
# circle.display()
# circle.draw()

class BankAccount:
    def _init_(self,ac_no,balance=0):
        self.__ac_no = ac_no
        self.__balance = balance
    def deposit(self,deposit):
        self.__balance = self.__balance+deposit
        print(self.deposit)
    def withdraw(self,withdraw):
        self.__balance = self.__balance - withdraw
        print(self.withdraw)
obj = BankAccount()
obj.deposit(100)
obj.withdraw(20)