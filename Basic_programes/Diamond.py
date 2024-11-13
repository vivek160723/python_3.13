n=5
for i in range (n-1):
    for j in range (1,n-i):
        print("  ",end=" ")
    for j in range(i):
        print(" *",end=" ")
    for j in range(i+1):
        print(" *",end=" ")
    print()
for i in range(n):
    for v in range(i):
        print("  ", end=" ")
    for j in range(1, n - i):
        print(" *", end=" ")
    for j in range(n - i):
        print(" *", end=" ")
    print()