# s="nitin"
# ans=s[::-1]
# if(ans==s):
#  print("yes it is palindrome")
# else:
#     print("no its not palindrome")

#################################################################################################
s = "nitin"
ans = ""
for i in s:
    ans = i + ans
if s == ans:
    print("yes")
else:
    print("not")
#################################################################################################
s = "nitin"
s2 = ""
for i in s:
    s2 = i + s2
if s == s2:
    print("It is a palindrome:", s)
else:
    print("It is not a palindrome:", s)