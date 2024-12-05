# main.py

import math_operations

def badmash():
    a = 10
    b = 5

    print(f"{a} + {b} = {math_operations.add(a, b)}")
    print(f"{a} - {b} = {math_operations.subtract(a, b)}")
    print(f"{a} * {b} = {math_operations.multiply(a, b)}")

    if b != 0:
        print(f"{a} / {b} = {math_operations.divide(a, b)}")
    else:
        print("Division by zero is not allowed.")
badmash()