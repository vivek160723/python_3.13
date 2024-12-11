import math

num1=int(input("Enter the number:"))
try:
    if num1<0:
        raise ValueError("Number must be positive")
    else:
        print(math.sqrt(num1))
except Exception as e:
    print(e)