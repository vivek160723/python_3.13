my_tuple = (10, 20, 30, 56, 40)
my_list = list(my_tuple)
minn = my_list[0]
maxx = my_list[0]

for i in my_list:
    if i > maxx:
        maxx = i
    if i < minn:
        minn = i

my_list.remove(minn)
my_list.remove(maxx)
ans=tuple(my_list)
print(ans)


print("-------------------------------------------------")
Myset = {1, 2, 3, 4, 5}
maxi = float('-inf')
mini = float('inf')
for i in Myset:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
Myset.remove(mini)
Myset.remove(maxi)
print(Myset)