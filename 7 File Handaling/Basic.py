Name=input("Enter Name = ")
Email=input("Enter Email = ")
Address=input("Enter Address= ")
Birth=input("Enter Birth= ")

s="Name="+Name+"\n\nEmail="+Email+"\n\nAddress="+Address+"\n\nBirth="+Birth
a=str(input("Enter File Name : "))
f=open(a+".txt","w")

f.write(s)

print("file successfully created...")

f.close()