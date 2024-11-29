import array
array=array.array("i",[1,2,3,4,5])
n=int(input("Enter the nth: "))
ans1=array[n:]+array[:n]
print(ans1)