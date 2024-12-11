# class GetterSetterExample:
#     def __init__(self, name, age):
#         self.__name = name  # Private attribute
#         self.__age = age  # Private attribute
#
#     # Getter for name
#     def get_name(self):
#         return self.__name
#
#     # Setter for name
#     def set_name(self, name):
#         self.__name = name
#
#     # Getter for age
#     def get_age(self):
#         return self.__age
#
#     # Setter for age
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             raise ValueError("Age must be positive")
#
#
# person = GetterSetterExample("Vivek", 23)
# print(person.get_name())
# print(person.get_age())

class GetterSetterExample:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Setter for name
    @name.setter
    def name(self, name):
        self.__name = name

    # Getter for age
    @property
    def age(self):
        return self.__age

    # Setter for age
    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive")


# Example usage
person = GetterSetterExample("Vivek", 23)
print(person.name)  # Output: Vivek
print(person.age)   # Output: 23

# Using setters to update values
person.name = "Rahul"
person.age = 25

print(person.name)  # Output: Rahul
print(person.age)   # Output: 25
