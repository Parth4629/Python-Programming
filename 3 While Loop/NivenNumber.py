a=int(input("Enter The Value : "))
s=0
i=a

while(i>0):
    t=i%10
    s=s+t
    i=i//10
if (a%s==0):
    print(a,"This Niven Number")
else :
    print(a,"Not Niven Number")
    