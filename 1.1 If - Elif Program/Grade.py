a = int(input("Enter the value ="))
b = int(input("Enter the value ="))
c = int(input("Enter the value ="))
d = int(input("Enter the value ="))
e = int(input("Enter the value ="))

t=a+b+c+d+e


print("sum",t)


avg=t/5

print("avg marks=",avg)

if avg>=70:
    print("Grade=A")
elif avg>=60:
    print("Grade=B")
elif avg>=50:
    print("Grade=C")
elif avg>40:
    print("Grade=D")
elif avg<=35:
    print("Sorry You are a Fail")  
    