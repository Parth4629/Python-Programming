a=int(input("Enter Size : "))
b=input("Enter Character Name : ")

f=open("Kite Example.txt","w")

for i in range(1,a):
      for k in range(1,a-i+1):
               f.write("  ")      
      for j in range(1,i+1):
               f.write(b+"   ")
      f.write("\n")

for i in range(a,0,-1):
      for k in range(1,a-i+1):
               f.write("  ")         
      for j in range(1,i+1):
               f.write(b+"   ")
      f.write("\n")

for i in range(2,a-2):
      for k in range(1,a-i+1):
               f.write("  ")    
      for j in range(1,i+1):
               f.write(b+"   ")
      f.write("\n")
         
f.close()

print("file successfully created...")

