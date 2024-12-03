# class Counter:
#     count = 0
#
#     @classmethod
#     def create_object(clsi):
#         clsi.count += 1
#         print("Total objects created:", clsi.count)
#         return clsi()
#
# obj1 = Counter.create_object()  # Create first object
# obj2 = Counter.create_object()  # Create second object
# obj3 = Counter.create_object()  # Create third object
##############################################################################################
class task8:
    count=0
# class varible are the static one
    def m1(self):
        task8.count+=1
        print(task8.count)

obj1=task8()
obj2=task8()

obj1.m1()
obj1.m1()
obj1.m1()
obj2.m1()
