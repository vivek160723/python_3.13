def perform_operations():
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        try:
            result = num1 / num2
            print(f"Division result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        my_list = [10, 20, 30, 40, 50]
        index = int(input("Enter the index of the list element to retrieve: "))
        try:
            element = my_list[index]
            print(f"Element at index {index}: {element}")
        except IndexError:
            print(f"Error: Index {index} is out of bounds for the list.")
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")
    finally:
        print("Operation completed.")

perform_operations()