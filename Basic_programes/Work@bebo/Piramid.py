N=5
for i in range (N):
    for j in range(1,N-i):
        print(" ",end=" ")
    for k in range(i):
        print("*", end=" ")
    for l in range(i+1):
        print("*", end=" ")
    print()