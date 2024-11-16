# s='vivek bad-mash '
# g='gaurav noob'
# print(g)
# #  g[0]='r' this will not change as strings are immutable
# name=str()
# #strings are immutable in python
# print(id(g))
# a=4
# b=4
# print(id(a))
# print(id(b))
# # +
# print(s+g)
# print(s*10,)
#
# print(g[0:-2])
#
# print(chr(65))
print(ord("A"))
# print(max('welcometopython'))
# print(len('vivek'))
# print('viv'in s)
#
# print('tie'=='mie')
# if 'vivek'>'gaurav':
#     print("vivek is powerful")
#
# print('Gauravmaan'<'vivekchaudhary')
#
# print('india'>'bharat')
# print('')

###################################----Testing the strings 13 november-----###############################
s="vivek"
print(s.isalnum())

s="welcome to python"
print(s.isalpha())

s="Gauravisnoob"
print(s.isalnum())

s="12345"
print(s.isdigit())
#
s="bebop"
print(s.isidentifier())

s="vivek"
print(s.isupper())

s="vivek"
print(s.islower())

s=" "
print(s.isspace())
#>>>>>>>>>>>>>>>>------------------ for searching in string --------------------------->>>>>>>>
print("<--------------------------------------------------------------------------------------->")
s="vivek"
print(s.endswith("ek"))

s="vivek"
print(s.startswith("ek"))

s="vivek"
print(s.find("ek"))

s="vivek"
print(s.find("r"))

s="vivekekekekek"
print(s.index("e"))

s="vivek"
print(s.count("ek"))

s="gauravmaan"
print(s.count("a"))

#>>>>>>>>>>>>>>>>------------------ for searching in string --------------------------->>>>>>>>

s="welcome to battleground"

print(s.capitalize())
print(s.title())
print(s.lower())
print(s.swapcase())
print(s.upper())
print(s.replace("to","in"))
