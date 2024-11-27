def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test the function
ans=factorial(5)
print(ans)