try:
    x=int(input("Enter the first number:"))
    y=int(input("Ente the second number:"))
    if x or y <0:
        raise ValueError("yoo")
    else:
        print(x+y)
except ValueError as e:
    print(f"Exception caught: {e}")


