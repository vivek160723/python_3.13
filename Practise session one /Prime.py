N = int(input("Enter the number:"))
prime = True
if N <= 1:
    prime = False
else:
    for i in range(2, int(N/2) + 1):
        if N % i == 0:
            prime = False
            break
if prime:
    print("It's a prime number.")
else:
    print("Not a prime number.")

