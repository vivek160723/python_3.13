value = input("Enter a number: ")
if value == value[::-1]:
    print(f"{value} is a palindrome.")
else:
    print(f"{value} is not a palindrome.")
