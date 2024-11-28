# def fun(n):
#     return lambda x:x-n
#
# ans=fun(10)
# print(ans(11))


# def myfunc(n):
#   return lambda a : a * n
#
# doubler = myfunc(2)
# print(doubler(11))

def fun1(x):
    def fun2(a):
        return fun1+fun2

print(fun1(1))