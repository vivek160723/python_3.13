# 3 types of error :syntax error, logical error, run_time error
# this is very important

# try:
#     # Code that may raise an exception
# except ExceptionType:
#     # Code to handle the exception
# else:
#     # Code to execute if no exception occurs (optional)
# finally:
#     # Code that will execute regardless of whether an exception occurred or not (optional)
####--------Example 1: Basic Exception Handling-------#####
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("Operation successful!")
finally:
    print("Execution completed.")
#
# ####--------Example 2: Catching Multiple Exceptions-------#####
# try:
#     items = [1, 2, 3]
#     print(items[5])  # IndexError
# except (IndexError, KeyError) as e:
#     print(f"Caught an exception: {e}")
#
# ####--------Example 3: Using finally for Cleanup-------#####
# try:
#     file = open("example.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Error: File not found.")
# finally:
#     print("Closing the file.")
#     file.close()
#
# ####--------Example 4: Raising Exceptions-------#####
#
# def validate_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative!")
#     print("Valid age:", age)
#
# try:
#     validate_age(-5)
# except ValueError as e:
#     print(e)
# #
# # Key Concepts:
# # try block: Code that might cause an exception.
# # except block: Handles the exception; specific exception types can be caught.
# # else block: Executes if no exception occurs.
# # finally block: Executes regardless of whether an exception occurred (used for cleanup).
# # Custom Exceptions: You can define your own exception classes for specific use cases.
#
# #       Example of a Custom Exception
#
# class NegativeValueError(Exception):
#     pass
#
# def check_value(value):
#     if value < 0:
#         raise NegativeValueError("Value cannot be negative!")
#
# try:
#     check_value(-10)
# except NegativeValueError as e:
#     print(e)
#
