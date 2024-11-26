#positonal arguments

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

print(practice(i=0,))
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





















