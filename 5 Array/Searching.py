a=[0]
n=int(input("Enter n Value: "))

for i in range(n):
    b=input("enter name = ")
    a.append(b)

d=[0]

c=input("Enter search Name:")

for i in range(n):
    if a[i]==c:
        d=1
if d==1:
  print("Data Found")
else :
  print("Data Not Found")