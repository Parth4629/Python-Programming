a=int(input("Enter Size : "))
b=input("Enter character : ")

def Kite(a):

    for i in range(1,a):
         for k in range(1,a-i+1):
                 print("  ",end="")    
         for j in range(1,i+1):
                 print(b,end="   ")
         print("")

    for i in range(a,0,-1):
         for k in range(1,a-i+1):
                print("  ",end="")         
         for j in range(1,i+1):
                print(b,end="   ")
         print("")

    for i in range(2,a-2):
         for k in range(1,a-i+1):
                 print("  ",end="")    
         for j in range(1,i+1):
                 print(b,end="   ")
         print("")  

Kite(a)