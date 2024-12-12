class Student:
    marks=90
    def __init__(self,name,increment):
        Student.marks+=increment
        print(name,Student.marks)

obj1=Student("vivek",30)
