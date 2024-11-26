def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:

    choice = input("Enter choice (1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))

        # Ask if the user wants another calculation
        next_calc = input("Do you want to calculate again? (yes/no): ")
        if next_calc.lower() != "yes":
            print("Goodbye!")
            break
    else:
        print("Invalid input. Please select 1, 2, 3, or 4.")
