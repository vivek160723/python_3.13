def sort_numbers(Data):
    n = len(Data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if Data[j] > Data[j + 1]:
                Data[j], Data[j + 1] = Data[j + 1], Data[j]

numbers = [5, 4, 3, 2, 1]
print(f"Unsorted list: {numbers}")
sort_numbers(numbers)
print(numbers)

