print("pt-32")
c=1

for i in range(4,0,-1):
      for k in range(1,5-i+1):
             print("  ",end="")
             
      for j in range(1,i+1):
             print(c,end=" ")
             c=c+1
      print("")