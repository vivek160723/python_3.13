my_tuple=tuple(map(int,input("Enter the tuple:").split()))
min_val=my_tuple[0]
max_val=my_tuple[0]
for i in my_tuple:
    if i<min_val:
        min_val=i
    if i>max_val:
        max_val=i
print(f"The mix and max value are",(min_val,max_val))