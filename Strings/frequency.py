st2="aabbbccc"
ans={}
for i in st2:
    if i in ans:
        ans[i]+=1
    else:
        ans[i]=1
print(ans)
