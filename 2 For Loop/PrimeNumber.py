a=int(input("Enter the value : "))
t=0

for i in range(2,a):
     if (a%i)==0:
         t=1

if(t==1):
    print(a,"Not Prime Number")

else :
    print(a,"Prime Number") 