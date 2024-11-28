def sod(n):
    if n == 0:
        return 0
    return n % 10 + sod(n // 10)

number = int(input("Enter the number: "))
result = sod(number)
print("Sum of digits:", result)