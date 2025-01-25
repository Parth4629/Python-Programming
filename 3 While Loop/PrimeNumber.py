a=int(input("Enter the value : "))
t=0
i=2

while (i<a):
    if (a%i)==0:
         t=1
         
    i=i+1
    

if(t==1):
    print(a,"Not Prime Number")

else :
    print(a,"Prime Number") 
        


