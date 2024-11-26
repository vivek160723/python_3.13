def fun(n):
    return lambda x:x-n

ans=fun(10)
print(ans(11))