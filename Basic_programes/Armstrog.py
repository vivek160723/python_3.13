num = int(input("Enter the number: "))
temp = num
n = len(str(num))
ans = 0
while num > 0:
    ans += (num % 10) ** n
    num //= 10
if temp == ans:
    print("Yes, it is an Armstrong number")
else:
    print("Not an Armstrong number")
