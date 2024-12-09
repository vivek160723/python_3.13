# python does not support method overloading concept
class Parent:
    def display(self, x=None, y=None):
        if x is None and y is None:  # If no arguments are passed
            print("hello noob ke sath baithe hue pro player")
        elif x is not None and y is not None:  # If both x and y are passed
            print(x + y)
        else:
            print("Invalid inputs!")

# Instantiate and test
obj1 = Parent()
obj1.display()        # Output: hello noob ke sath baithe hue pro player
obj1.display(2, 3)    # Output: 5
