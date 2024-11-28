def outer(arg1):
    def inner(arg2):
        return f"{arg1} {arg2}"
    return inner

ans1 = outer("Hello")
ans2 = ans1("World")
print(ans2)