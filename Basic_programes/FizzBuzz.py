n = int(input("Enter the nth term: "))
ans = ""

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        ans += "fizzbuzz"
    elif i % 3 == 0:
        ans += "fizz"
    elif i % 5 == 0:
        ans += "buzz"
    else:
        ans += str(i)
    ans += " "

print("Result:", ans.strip(),end=" ")
