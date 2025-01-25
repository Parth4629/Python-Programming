a= int(input("Enter the value ="))
b= int(input("Enter the value ="))
c= int(input("Enter the value ="))



if a > b and a > c:
    print("a is maximum")

elif b > a and b > c:
    print("b is maximum")
elif c > a and c > b:
    print("c is maximum")    

elif a==b and b==c:
    print("All value same")
