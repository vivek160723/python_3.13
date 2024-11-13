print("please enter your age:")
age=int(input())
if(age>=18):
    print("Do you have a driving license (yes/no)?")
else:
    print("you are not eligible")
ans=input()
if(ans=="yes"):
    print("you are ready to drive")
else:
    print("you are not eligible")

