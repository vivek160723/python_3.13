num = int(input("Enter an integer: "))
sum1 = 0
while num > 0:
    sum1 += num % 10
    num //= 10
num = sum1
print(f"The single-digit sum is {num}")