def evoked(num):
    ans=False
    if num % 2==0:
        ans=True
    return ans

n=int(input("Enter the number:"))
print(evoked(n))