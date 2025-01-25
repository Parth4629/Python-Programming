a=int(input("Enter The Value : "))
b=0
i=1

while (i<a):
   if(a%i==0):
    b=b+i
   i=i+1
     
if(b==a): 
    print("Perfect Number")
else:
    print("Not Perfect Number")  
