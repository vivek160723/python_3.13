# import array
# creating an array
# arr=array.array(typecode.[element])
# common typecode:
# i=signed integers
# I=unsigned integers
# f=floating integers
# d=double

import array  # Import the array module to work with arrays.

# Create an array of integers with the typecode "i" (signed integer) and initial elements.
arr1 = array.array("i", [1, 3, 4, 5])

# Iterate through the array and print each element, separated by spaces.
for i in arr1:
    print(i, end=" ")

# Print a newline and then the first element of the array.
print("\n", arr1[0])

# Append the value 4 to the end of the array.
arr1.append(4)

# Remove the first occurrence of the value 1 from the array.
arr1.remove(1)

# Count how many times the value 4 occurs in the array and print it.
print(arr1.count(4))

# Remove and return the element at index 3 (fourth element in the array).
arr1.pop(3)

# Extend the array by appending elements from the list [7, 8, 9].
arr1.extend([7, 8, 9])

# Insert the value 39 at index 0 (the beginning of the array).
arr1.insert(0, 39)

# Print the updated array to display all its elements.
print(arr1)

print(arr1.buffer_info())

print(arr1.index(4))