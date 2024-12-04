def sum3(*args):
    ans=0
    for x in args:
        ans+=x**2
    return ans

result=sum3(1,2,3)
print(result)
