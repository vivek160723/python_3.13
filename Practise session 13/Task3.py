import array
arr1 = array.array("i", [1, 3, 4, 5])
try:
    print(arr1[5])
except Exception as e:
    print(e)
