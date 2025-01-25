class Customer:
    def Coust(self):
        self.Cname=str(input("Enter The Coustomer Name : "))
        self.Email=str(input("Enter The Email id : "))

class Product(Customer):
    def Pro(self):
        self.Pname=str(input("Enter The Product name : "))
        self.Qty=int(input("Enter The Quantity : "))
        self.price=int(input("Enter The Price : "))
        
class Total(Product):
    def To(self):
        self.Tprice=self.price*self.Qty

        if self.Tprice>=3000:
            per=20
        elif self.Tprice>=2000:
            per=15
        elif self.Tprice>=1500:
            per=10
        elif self.Tprice>=1000:
            per=5
        else :
            per=0
        
        self.Dis=self.Tprice*per/100
        self.Net=self.Tprice-self.Dis

class Shopping(Total):
    def Shop(self):
        print("\nCustomer Name: ",self.Cname)
        print("Email-Id : ",self.Email)
        print("Price: ",self.price)
        print("Quantity: ",self.Qty)
        print("Total Price: ",self.Tprice)
        print("Discount: ",self.Dis)
        print("Net Price: ",self.Net)

    
d = Shopping()

d.Coust()
d.Pro()
d.To()
d.Shop()