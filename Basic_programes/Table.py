#print the table of the given number

N=int(input("Enter the number:"))
ans=0
i=1
for i in range(1,11):
    print(f"{N}x{i}=",N*i)
