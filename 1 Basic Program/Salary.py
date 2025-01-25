a = str(input("Enter Employee Name : "))
b = int(input("Enter Employee Salary : "))

c=b*10/100
d=b*5/100

print("Hra (10%) =",c)
print("Da (5%) =",d)


t=b+c+d
print("Total Salary : ",t) 

e=t*6/100
print("Pf (6%) =",-e)

s=t-e
print("Net salary : ",s)


print("\tEName\tSalary\tHRA\tDa\tNet Salary")

print("\t",a,"\t",b,"\t",c,"\t",d,"\t",s)