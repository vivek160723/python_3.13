num=int(input())
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
else:
    print("it is a prime number")