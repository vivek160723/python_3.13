numbers = [10, 20, 4, 45, 99]
if len(numbers) < 2:
    print("Not enough elements to find the second largest number.")
else:
    largest = numbers[0]
    second_largest = None

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or (num > second_largest and num != largest):
            second_largest = num

    if second_largest is None:
        print("No second largest number found.")
    else:
        print("Second Largest:", second_largest)
