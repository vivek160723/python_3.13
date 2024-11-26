# def replace(s,a,c):
#     return ''.join(map(lambda char: c if char == a else char, s))
# x="vivek"
# y="k"
# z="v"
# print(replace(x,y,z))
#
# print("----------------------------------")



def ref(str1,ans1):
    for i in str1:
        if i==char1:
            ans1+=char2
        else:
            ans1+=i
    print(ans1)

sentence="vivek"
ans=""
char1="k"
char2="t"
ref(sentence,ans)