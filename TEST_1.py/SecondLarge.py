my_list=[4,7,5,6,4,5,4]
largest = my_list[0]
sec = 0
for i in my_list:
    if i>largest:
        sec = largest
        largest=i
    elif sec < i < largest:  # elif i>sec and i<largest:
        sec=i
print(sec)

