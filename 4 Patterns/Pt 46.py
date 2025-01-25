print("pt-46")
for i in range(1,5):
     for j in range(1,5):
          if i==2 and j==2:
                print("4  ",end="")
          elif i==2 and j==3 or i==3 and j==2 :
                print("6  ",end="")
          elif i==3 and j==3 :
                print("12 ",end="")
          else:
                print("1  ",end="")
     print("")