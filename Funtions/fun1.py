# If you want to use any function to this package in your right next is your user, so we are going to learn
# Define function how to create user define functionality. What are the different way how to pass the argument and what are the different type of arguments?
# functions are reusable
# function can take input(called parameter or arguments)
# code reusability improve readability or give the clear understanding on the logic
# easier debugging
#
# types of function:
# function does not argument do not return any value #none
# functions no argument but return type
# argument but no return type
# argument and return type both are there


def fun():
    print("hello brother")  #cLLING HAPPENS DIRECTLY FROM THE INTERPRETER
fun()
#----------------------------------------------------------------------------
print("-----------------------------------------------------------------")
def fun2(nname):
    print("Helllo",nname)
    return nname
dtr="vivek"
fun2(dtr)
#-----------------------------------------------------------------------------
print("-----------------------------------------------------------------")
def fun3(n,s):
    print("Helllo",n,s)
    return n,s


v="vivek"
p="chaudhary"
fun3(v,p)

print("-----------------------------------------------------------------")

def fun4(n,s):
    return(n+s)
print(fun4(1,2))

print("-----------------------------------------------------------------")

def fun4(n,s):
    print(n+s)
fun4(10,2)

