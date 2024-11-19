# list1 = input("Enter the list elements separated by spaces: ")
# nums = [int(x) for x in list1.split()]
# ans = []
# for i in list1:
#     duplicate = False
#     for j in ans:
#         if j == i:
#             duplicate = True
#             break
#     if not duplicate:
#         ans.append(i)
#
#
# print("Original List:", list1)
# print("List Without Duplicates:", ans)

print("--------------------------------------------------------------------------")
#
# list1=[1,2,3,4,2,2,4,4,6,7,8,8,9]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)
#
print("--------------------------------------------------------------------------")


my_list = [1, 1, 2, 3, 4, 5]
i = 0
while i < len(my_list):
    j = i + 1
    while j < len(my_list):
        if my_list[i] == my_list[j]:
            my_list.pop(j)
        else:
            j += 1
    i += 1
print(my_list)
