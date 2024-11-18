my_tuple=(10,20,74,18,37)
min_val=my_tuple[0]
max_val=my_tuple[0]
for ele in my_tuple:
    if ele<min_val:
        min_val=ele
    if ele>max_val:
        max_val=ele
print(f"The mix and max value are",(min_val,max_val))