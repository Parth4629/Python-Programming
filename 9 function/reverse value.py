a=int(input("Enter the Value : "))

def Reverse(a):
    i=0
    s=0

    while(a>0):
         t=a%10
         s=s+t
         print(t,end="")
         a=a//10
    print("\nTotal Sum =: ",s)

Reverse(a)