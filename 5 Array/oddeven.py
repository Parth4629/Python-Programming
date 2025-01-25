a=[]
OC=0
OS=0
EC=0
ES=0


n=int(input("Enter n Value :"))
for i in range(n):
    b=int(input("enter value = "))
    a.append(b)

print("Odd    Even")
for i in range(n) :
    if(a[i]%2==1):
         OC =OC+1
         OS =OS+a[i]
         print(a[i],end="\t")

    else:
        EC =EC+1
        ES =ES+a[i]
        print(a[i])


print("\n\nOdd Count : ",OC,"\t\tSum Of Odd : ",OS,"\nEven Count : ",EC,"\tSum Of Even : ",ES)


