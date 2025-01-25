a=int(input("Enter The Value : "))
s=0
i=s
b=a
while(a>0):
    t=a%10
    s=s*10+t
    print(t,end="")
    a=a//10
print("\nTotal Sum =: ",s)

if (s==b):
   print("This Number Is Palindrome")
else :
    print("This Number Not Palindrome")
