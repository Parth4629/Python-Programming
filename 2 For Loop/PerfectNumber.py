a=int(input("Enter The Value : "))
b=0

for i in range(1,a):
  
  if(a%i==0):
    b=b+i
     

if(b==a): 
    print("Perfect Number")
else:
    print("Not Perfect Number")  