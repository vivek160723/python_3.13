#it can take any no of function
# generally used filter() map() and sorted()
#
# x=lambda a,b,c:a+b+c
# print(x(10,20,400))
#
# my_list=[7,20,30]
# ans=[]
# for i in my_list:
#     if i%2==0:
#         ans.append(i)
# print(ans)

# even_no=list(filter(lambda x:x%2==0,my_list))
# print(even_no)

# print("-----------------")
#
# city=["chandigarh","goa","delhi"]
#
# # def length(city):
#     return len(city)
# sort=sorted(city,key=length,reverse=False)
# print(sort)

# # sort=sorted(city,key=lambda x:len(x))
# # print(sort)
#
# my_list2=[2,3,4,5]
# # even_no=set(map(lambda x:x**2,my_list2))
# # print(even_no)
#
# from functools import reduce
# z=reduce(lambda x,y:x+y,my_list2)
# print(z)
#

# zip()

a=["a","b","c","d","e","f"]
b=[7,6,5,7]
ans=zip(a,b)
print(list(ans))