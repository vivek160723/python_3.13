#reverse of a number using while loop and counting the digits in the number.
num = int(input("Enter a number: "))
reverse = 0


while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10


print("Reversed number:", reverse)
