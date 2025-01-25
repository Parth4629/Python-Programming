print("***** Shopping System *****")
a = str(input("Enter Customer Name : "))
b = str(input("Enter Product Name : "))
c = int(input("Enter Product Qty : "))
e = int(input("Enter Product Price : "))

t=e*c

print("Total=",t)

d=0
if t>=1500:
    d=t*15/100
    print("Discount (15%)",d,)
elif t>=1000:
    d=t*10/100
    print("Discount (10%)",d,)
elif t>=500:
    d=t*5/100
    print("Discount (5%)",d,)
elif t<=500:
    print("Discount (0%)")    


print("Net Price=",t-d)
