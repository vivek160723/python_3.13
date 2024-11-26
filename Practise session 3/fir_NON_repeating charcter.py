str=input("Enter the string: ")
store={}
for i in str:
    if i in store:
        store[i]+=1
    else:
        store[i]=1
for char in store:
    if store[char]==1:
        print(f"{char}")
        break
else:
    print("There are no repeating chracters")