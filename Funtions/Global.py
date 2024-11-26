# global variable u can access it from anywhere
# local variable limited to that functions only
#
# global_var=20  # This is global variable here
# def my_fun():
#     lv=10# this is local variable
#     print(lv)
#
# my_fun()
# print(global_var)
#
# print("-----------------------------")

lv=20  # This is global variable here
def coll():
    global lv# to change the value of the global variable inside the fucntion
    lv=1000# this is local variable
    print(lv)

coll()
print(lv)

print("-----------------------------")

