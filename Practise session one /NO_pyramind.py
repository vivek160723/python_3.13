N =int(input("Enter The number:"))
count = 1
for i in range(N):
    for j in range(1, N - i):
        print("  ", end=" ")
    for k in range(i):
        print(f"{count:2}", end=" ")
        count += 1
    for l in range(i + 1):
        print(f"{count:2}", end=" ")
        count += 1
    print()