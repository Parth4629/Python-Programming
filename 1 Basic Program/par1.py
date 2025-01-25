a = int(input("Enter The Value ="))
b = int(input("Enter The Value ="))

print("(1) for sum")
print("(2) for sub")
print("(3) for mul")
print("(4) for div")


ch=int(input("Enter Your Choice : "))

if ch==1:
    print("sum=",a+b)

elif ch==2:
    print("sub",a-b)

elif ch==3:
    print("mul",a*b)

elif ch==4:
    print("div",a/b)

elif ch>4 or ch<0:
    print("invalid choice")