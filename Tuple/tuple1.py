my_tuple = (1, 2, 3, 4, 5)
# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

print("-------------------------------------------------------------------------------")

# Slicing a tuple
print("First three elements:", my_tuple[:3])
print("-------------------------------------------------------------------------------")

# Tuples can hold multiple data types
mixed_tuple = (1, "hello", 3.14)
print("Mixed tuple:", mixed_tuple)
print("-------------------------------------------------------------------------------")


# Unpacking a tuple
a, b, c = mixed_tuple
print("Unpacked values:", a, b, c)
print("-------------------------------------------------------------------------------")


# Iterating through a tuple
print("Iterating through the tuple:")
for item in my_tuple:
    print(item)
print("-------------------------------------------------------------------------------")


# Tuple with a single element (note the comma!)
single_element_tuple = (42,)
print("Single element tuple:", single_element_tuple)
print("-------------------------------------------------------------------------------")


# Checking the length of a tuple
print("Length of my_tuple:", len(my_tuple))

print("-------------------------------------------------------------------------------")

my_tuple2=(1,"vivek",3,4.45)
print(my_tuple2)
my_list=list(my_tuple2)
print(my_list)
my_list[1]="rahul"
print(my_list)
ans2=tuple(my_list)
length=(len(my_tuple2))
print(length)