def binary_search(data, target):
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if data[mid] == target:
            return mid  # Target found, return index
        elif data[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found


# Example usage
data = [1, 2, 3, 3, 3, 4, 5, 6]  # Sorted list
target = 5
result = binary_search(data, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found.")