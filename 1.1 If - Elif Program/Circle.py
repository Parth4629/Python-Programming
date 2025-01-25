print("(1) Find Out Of the area Of Circle")
print("(2) Find Out Of the area Of Triangle")
print("(3) Find Out Of the area Of Square")
print("(4) Find Out Of the area Of Rectangle")


ch=int(input("enter your choice :"))

if ch==1:
    r=int(input("enter radius="))
    print("area of circle=",3.14*r*r)

elif ch==2:
    h=int(input("enter hight of triangle="))
    b=int(input("enter bredth of triangle="))
    print("area of Triangle=",h*b*0.5)

elif ch==3:
    h=int(input("enter hight of triangle="))
    b=int(input("enter bredth of triangle="))
    print("area of Square =",h*b)

elif ch==4:
    l=int(input("enter the langht Of Square="))
    print("area of Square=",l*l)