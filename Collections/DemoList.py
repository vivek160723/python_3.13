# list1=[1,2,3,4,5]
# list2=['strawberry','banana','avocado','strawberry','banana','avocado']
# list3=['pineapple',1001001,10.21,]
# list4=list()
#
# print("--------------------------------------------------------------------------------------------")
# print(list3)
#
# print("--------------------------------------------------------------------------------------------")
# print(list2[2])
#
# print("--------------------------------------------------------------------------------------------")
# print(list1[1:4])
# print(list2[-4:-1])
#
# print("--------------------------------------------------------------------------------------------")
#
# list1[0]=98
# print(list1)
# print("--------------------------------------------------------------------------------------------")
# for i in list1:
#     print(i)
#
#
# print("--------------------------------------------------------------------------------------------")
#
# if "avocado" in list2:
#     print("Guarav is noob")
# print(len(list1))
#
# print("--------------------------------------------------------------------------------------------")
#
# list1.append(56)
# print(list1)
#
# list1.insert(2,78)
# print(list1)
#
#
# print("--------------------------------------------------------------------------------------------")
#
# list1.pop(3)
# print(list1)
#
# print("--------------------------------------------------------------------------------------------")
# del(list1)
# list1.clear()

# my_list=["vivek",23,"gaurav",22]
# empty_list=list(my_list)
# print("------")
# print(empty_list)
# print(my_list)
# print("------")
# my_list1=my_list.copy()
# print(my_list1)
# my_list2=my_list+my_list1
# print(my_list2)

#append used in list to add to specific index
# Creating a list
# my_list = [1, 2, 3]

# Appending an element to the list
# my_list.append(4)
#
# print("After appending 4:", my_list)
#
# # Appending multiple elements using extend()
# my_list.extend([5, 6, 7])
# print("After extending:", my_list)
#
# # Appending a list as a single element
# my_list.append([8, 9])
# print("After appending a list:", my_list)
#
# user_list=input().split(" ")
# print(user_list)

a=list(map(int,(input().split(" "))))
# print(a.count(4))
print("----------------------------")
a.sort()
print(a)

print("----------------------------")
a.sort(reverse=True)
print(a)

print("----------------------------")
