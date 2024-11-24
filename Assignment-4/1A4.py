# Input the list of numbers and the target number to remove
numbers = [int(x) for x in input("Enter a list of "
"numbers separated by spaces: ").split()]
target = int(input("Enter the number to remove: "))

# Remove all occurrences of the target number
while target in numbers:
    numbers.remove(target)

# Print the modified list
print("Modified list:", numbers)
