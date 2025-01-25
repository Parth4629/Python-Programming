a=[]


n=int(input("Enter n Value :"))
for i in range(n):
    b=int(input("enter value = "))
    a.append(b)

pos=a[0]
Neg=a[0]


for i in range(n):
    if a[i] > 0:
       pos=a[i]
    elif a[i] < 0:
       Neg=a[i] 

print("\nPositive Value ",pos)
print("Negative value",Neg)




