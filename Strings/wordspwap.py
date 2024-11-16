# s=(input("Enter the string"))
# rev_string=" "
# for i in s:
#     rev_string=i+rev_string
# print(rev_string)

# s = input("Enter the string: ")
# rev_string = ""
# word = ""
#
# for i in s:
#     if i != " ":
#         word = i + word
#     else:
#         rev_string += word + " "
#         word = ""
#
# rev_string += word
# print(rev_string)

s = (input("Enter the string:"))
ans = s.split()
for i in s:
    r = i[-1::-1]
print(r, end=" ")
