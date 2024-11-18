# list = input("Enter the list elements separated by spaces: ")
# nums = [int(x) for x in list.split()]
# ans = []
# for i in list:
#     duplicate = False
#     for j in ans:
#         if j == i:
#             duplicate = True
#             break
#     if not duplicate:
#         ans.append(i)
#
#
# print("Original List:", list)
# print("List Without Duplicates:", ans)

print("--------------------------------------------------------------------------")

list1=[1,2,3,4,2,2,4,4,6,7,8,8,9]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

