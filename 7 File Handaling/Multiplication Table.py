c=""

a=int(input("Enter The Value a: "))
b=int(input("Enter The Value b: "))
for i in range(a,b+1):
    for j in range(1,11):
         result=i*j
         c=c+str(i)+"x"+str(j)+"="+str(result)+"\n"
   
f=open("Multiplication.txt","w")
f.write(c)
       
f.close()

print("file successfully created...")


