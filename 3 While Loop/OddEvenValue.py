a=int(input("Enter The Value : "))

OC=0
OS=0
EC=0
ES=0

i=0



print("Odd    Even")
while(i<a):
     i=i+1
     if(i%2==1):
         OC =OC+1
         OS =OS+i
         print(i,end="\t")


     else:
        EC =EC+1
        ES =ES+i
        print(i)


print("\n\nOdd Count : ",OC,"\t\tSum Of Odd : ",OS,"\nEven Count : ",EC,"\tSum Of Even : ",ES)

    
