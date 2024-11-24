# Input: tuple of numbers
numbers_tuple = (1, 2, 3, 4)

# Number to append
number_to_append = 5

# Convert the tuple to a list
numbers_list = list(numbers_tuple)

# Append the given number to the list
numbers_list.append(number_to_append)

# Convert the list back to a tuple
updated_tuple = tuple(numbers_list)

# Print the updated tuple
print("Updated tuple:", updated_tuple)
