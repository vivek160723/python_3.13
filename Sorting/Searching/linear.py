data = [1, 3, 2, 3, 4, 6, 3, 5]
trgt = 5
found = False

for index in range(0,len(data)):
    if data[index] == trgt:
        found = True
        print(f"We found the element at index {index}")
        break

if not found:
    print("Element not found.")