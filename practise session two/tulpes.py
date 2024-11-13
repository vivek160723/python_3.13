my_tuple = (1, 2, 3, 4, 5)

# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)

print(my_tuple[0])
print(mixed_tuple[1])

print(my_tuple[1:4])

# Counting occurrences of a value
print(my_tuple.count(3))

# Finding the index of a value
print(my_tuple.index(4))

# my_tuple[0] = 10  # This will raise a TypeError

a, b, c, d, e = my_tuple
print(a)
print(b)
