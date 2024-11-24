#program to remove duplicate words from the string.

str1="i am am vivek."
str2=str1.split()
ans=[]
for i in str2:
    if i not in ans:
        ans.append(i)
print(" ".join(ans))
