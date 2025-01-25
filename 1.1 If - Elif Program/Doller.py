s=int(input("enter the value ="))

print("(1) D to Rs")
print("(2) Rs to D")
print("(3) Cm to Foot")
print("(4) Km to Foot")
print("(5) Pound to kg")
print("(6) F to C")
print("(7) Exit")


ch=int(input("enter your choice ="))

if ch==1:
   print("D to Rs",s*83.25)

elif ch==2:
   print("Rs to D",s*83.25)

elif ch==3:
   print("Cm to Foot",s*0.032800)

elif ch==4:
   print("Km to Foot",s*3280.8399)

elif ch==5:
   print("Pound to Kg",s*0.45359)

elif ch==6:
   print("F to C",(s-32)*5/9)

elif ch==7:
   print("Exit")
  