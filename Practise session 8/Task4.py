def max3(a,b,c):
    if a>b and a>c:
        return (f"{a} is greatest")
    elif b>a and b>c:
        return (f"{b}bis greatest")
    else:
        return (f"{c}is greatest")

ans=max3(40,30,30)
print(ans)