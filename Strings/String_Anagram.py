str1="listen"
str2="silent"
ans1={}
ans2={}
for i in str1:
    if i in ans1:
        ans1[i]+=1
    else:
        ans1[i]=1
for j in str2:
    if j in ans2:
        ans2[j]+=1
    else:
        ans2[j]=1
if ans1==ans2:
    print("yes they are anagram")
else:
    print("Noo the are not anagram")