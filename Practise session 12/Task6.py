class Accessorised:
    __name = "gaurav"  # Private
    _age = 34          # Protected

    def display(self):
        print(self.__name, self._age)

    def get_name(self):
        return self.__name


class Badman(Accessorised):
    def b1(self):
        print( self.get_name())
        print( self._age)


obj1 = Badman()
obj1.b1()
