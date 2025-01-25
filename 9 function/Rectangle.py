a=int(input("Enter The Value a: "))
b=int(input("Enter The value b: "))

def Rectangle(a):
    for i in range(1,a+1):
        for j in range(1,b+1):
            print("*",end=" ")
        print("")

Rectangle(a)