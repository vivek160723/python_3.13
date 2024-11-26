def myfunc(n):
  return lambda a : a * n

doubler = myfunc(2)
triple = myfunc(3)

print(doubler(11))
print(triple(10))