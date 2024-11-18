print("Enter the first value")
val1=int(input())
print('Enter the second value')
val2=int(input())
if(val1 > 0 and val2 > 0):
    print("They are positive")
elif(val1 < 0 and val2 < 0):
    print("they are negative")
else:
    print("They are mixed")