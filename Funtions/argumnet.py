#positional arguments

def fun4(n,s):
    print(n+s)
fun4(1,2)

print("---------------------------")
#keyword arguments
def fun3(n,s):
    print("hello",n,s)
    return n,s


v="vivek"
p="chaudhary"
fun3(v,p)
print("---------------------------")

#defult value
def practice(i,j=200):
    return i,j

print(practice(i=0))
print("---------------------------")
def allinone(name,msg):
     return name,msg
print(allinone("vivek","hii"))

print("---------------------------")
def wer(a,b,c):
     print(a,b,c)
# we can use the combination as well in calling the function with arguments
wer(3,10,c=20)

print("---------------------------")

# *args argument--positional variable length argument,
# allow a function to accept any no of positional arguments

# **kwargs arguments--keyword variable length arguments
#passed as tuple
def greet(*n):
    print("hello",{n})

greet("vivek","gaurav")

print("---------------------------")

def args(**n):
    for key,value in n.items():
        print(f"{key} {value}")


args(name="vivek",age =23,city="launchpad")
print("---------------------------")
def both(*x,**y):
    print(x)
    print(y)

both(1,2,3,4 ,name="vivek",age=23)
print("---------------------------")
def both2(name,*x):
    print(name)
    print(x)

both2("vivek","gaurav","noob",1,2,3,4,)



print("---------------------------")
def both3(n,*x,**y):
    print(n)
    for i in x:
        print(i)
    for i,j in y.items():
        print(f"{i} {j}")

both3("vivek",1,2,3,4 ,name="venom",city="pochinki",kd=-0.001)















