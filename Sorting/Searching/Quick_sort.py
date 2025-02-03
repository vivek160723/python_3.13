def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
numbers = [12, 4, 5, 6, 7, 3, 1, 15]
print("Unsorted list:", numbers)
sorted_numbers = quick_sort(numbers)
print("Sorted list:", sorted_numbers)
