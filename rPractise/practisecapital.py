# sen="i am vivek"
# ans=sen.split()
# longest=0
# longest_word=""
# for i in ans:
#     count=0
#     small=0
#     for j in i:
#         small+=1
#         if small>longest:
#             longest=small
#             longest_word=i
# print(longest)
# print(longest_word)

#
# sentence="i am vivek"
# ans=""
# for i in sentence:
#     ans=i+ans
# print(ans)


sentence="i am vivek"
res=sentence.split()
print(res)
ans2=[]
for i in res:
    ans = ""
    for j in i:
        ans=j+ans
    ans2.append(ans)
result=" ".join(ans2)
print(result)




