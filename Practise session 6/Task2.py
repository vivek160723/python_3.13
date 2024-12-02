class Student:
    name=""
    grade=""
    def display_info(self,name,grade):
        print(name,grade)

obj1=Student()
obj2=Student()

obj1.display_info("vivek",98)
obj2.display_info("gaurav",12)


#############################################################

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def display_info(self):
#         print(f"Student Name: {self.name}, Grade: {self.grade}")
#
# # Creating objects with different data
# obj1 = Student("Vivek", 98)
# obj2 = Student("Gaurav", 12)
#
# # Calling the method for both objects
# obj1.display_info()
# obj2.display_info()
