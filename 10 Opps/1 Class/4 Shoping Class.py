a=int(input("How Many Customer data insert ? : "))

class Shoping:
             
    def read(self):
        self.Cname=input("Enter The Customer Name : ")
        self.Product=input("Enter The Product Name : ")
        self.Price=int(input("Enter The Price : "))
        self.Qty=int(input("Enter The Quantity : "))
        self.Total=self.Price*self.Qty

        if  self.Total>=3000:
            per=20
        elif self.Total>=2000:
            per=15
        elif self.Total>=1500:
            per=10
        elif self.Total>=1000:
            per=5
        else :
            per=0

        self.Dis=self.Total*per/100
        self.Net=self.Total-self.Dis

    def show(self):
        print((self.Cname)+"\t\t\t"+str(self.Product)+"\t\t\t"+str(self.Price)+"\t\t"+str(self.Qty)+"\t\t"+str(self.Total)+"\t\t"+str(self.Dis)+"\t\t"+str(self.Net))

Shop=[]
for i in range(a):
    Shop.append(Shoping())

for dr in Shop:
    dr.read()

print("\nCustomer Name\t\tProduct Name\t\tPrice\t\tQuantity\tTotal Price\tDiscount\tNet Price")

for ds in Shop:
    ds.show()