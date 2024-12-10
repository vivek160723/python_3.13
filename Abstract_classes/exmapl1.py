from abc import *


class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def parameter(self):
        pass

class rectangle(shape):
    def area(self,widht,height):
        print(widht*height)
    def parameter(self,width,height):
        print(2*(width+height))

obj1=rectangle()
obj1.area(20,10)
obj1.parameter(2,5)