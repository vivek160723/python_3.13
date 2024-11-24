# write a program to capitalize the first letter of each word in a sentence
def capital(str1):
    str2=str1.split()
    ans=[]
    for i in str2:
        ans.append(i[0].upper()+i[1:])
    return " ".join(ans)


str="my name is kahna"
result=capital(str)
print(result)