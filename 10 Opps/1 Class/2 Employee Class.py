n=int(input("How many Employee data u want to insert ? : "))

class SalarySlip:

    def read(self):
        self.Employee=input("Enter Employee Name : ")
        self.Salary=int(input("Enter Salary : "))
        self.Hra=self.Salary*10/100
        self.Da=self.Salary*5/100
        self.Netsalary=self.Salary+self.Hra+self.Da

    def show(self):
        print(str(self.Employee)+"\t\t"+str(self.Salary)+"\t\t"+str(self.Hra)+"\t\t"+str(self.Da)+"\t\t"+str(self.Netsalary))

Salary=[]
for i in range(n):
    Salary.append(SalarySlip())

for dr in Salary:
    dr.read()

print("\nEmployee Name\tBasicSalary\tHra(10%)\tDa(5%)\t\tNetsalary")

for ds in Salary:
    ds.show()
    