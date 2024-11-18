print("Enter the marks in Maths:")
marks=int(input())
print("Enter the marks in science:")
marks1=int(input())
avg=marks+marks1/2
if(marks>=80 and marks1>=70):
    print("u are eligible")
elif(avg>=75):
    print("u are eligible")
else:
   print("sorry bro sad life u are not eligible")
