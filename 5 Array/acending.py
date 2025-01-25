n=int(input("Enter n Value :"))
a=[]

for i in range(n):
    b=int(input("enter valu e = "))
    a.append(b)


for i in range(n):
  for j in range(i+1,n):
    if(a[i]>a[j]):
       temp=a[i]
       a[i]=a[j]
       a[j]=temp

print("acending")
for i in range(n):
   print(a[i])



print("----------")



for i in range(n):
   for j in range(i+1,n):
      if(a[i]<a[j]):
         temp=a[i]
         a[i]=a[j]
         a[j]=temp
print("Decending")
for i in range(n):
   print(a[i])