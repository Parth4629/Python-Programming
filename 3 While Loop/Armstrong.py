a=int(input("Enter The Value : "))
s=0
i=s
b=a
while(a>0):
    t=a%10
    s=s+t*t*t
    a=a//10
if (s==b):
   print("This Number Is Armstrong")
else :
    print("This Number Not Armstrong")














