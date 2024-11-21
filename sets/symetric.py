set1=set(input("Enter the set"))
set2=set(input("Enter the set"))
ans=set1^set2
print(type(ans))
ans2=set1.symmetric_difference(set2)
print(ans2)