#print prime number between the range x,y
x=1
y=10
ans=[]
for i in range(x,y+1):
    if i>1:
        prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime=False
                break
        if prime:
            ans.append(i)
print(ans)



