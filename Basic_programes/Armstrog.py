n = int(input("Enter a number: "))
num = len(str(n))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** num
    temp //= 10
if sum == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")