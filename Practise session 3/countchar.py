s=input("Enter the string: ")
ans=""
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        ans+=s[i-1]+str(count)
        count = 1
ans += s[-1]+str(count)
print(ans)
