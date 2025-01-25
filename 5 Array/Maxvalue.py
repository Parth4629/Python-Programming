a=[]


n=int(input("Enter n Value :"))
for i in range(n):
    b=int(input("enter value = "))
    a.append(b)

max=a[0]
min=a[0]


for i in range(n):
    if a[i]>max :
        max=a[i]
    elif a[i]<min :
        min=a[i]

print("\nMax Value",max)
print("min Value",min)
        
    



