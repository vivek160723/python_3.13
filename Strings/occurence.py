s = input("Enter the string: ")
char_count = {}
for i in s:
    if i in char_count:
        char_count[i]+=1
    else:
        char_count[i]=1
print(char_count)


# for i in s:
#     found = False
#     for j in char_count:
#         if j == i:
#             char_count[j] += 1
#             found = True
#             break
#     if not found:
#         char_count[i] = 1
#
# for k in char_count:
#     print(f"{k}' appears {char_count[k]} times.")
