n=int(input("How many customer You Want to Enter:"))

class shoping:
    
    def custread(self):
        self.cname=input("Enter the Customer Name:")

    def custshow(self):
        print(self.cname)
        
    def proread(self):
        
        global a
        a=int(input("How Many Product you want to Enter:"))
        self.pname=[]
        self.price=[]
        self.quant=[]
        self.gt=0
        self.total=0
        for i in range(a):
            
            self.pname.append(input("Enter the Product Name:"))
            self.price.append(int(input("Enter the Price:")))
            self.quant.append(int(input("Enter the Quantity:")))
            self.total+=self.price[i]*self.quant[i]
        self.gt=self.gt+self.total
                

        if self.gt>=2000:

            per=20
    

        elif self.gt>=1500:
            per=15

        elif self.gt>=1000:
            per=10

        else :
            per=0

        self.dis=self.gt*per/100
        self.net=self.gt-self.dis
            

        

    def proshow(self):
        for i in range(a):
            print("\t"+str(i+1)+"\t"+self.pname[i]+"\t"+str(self.price[i])+"\t"+str(self.quant[i])+"\t"+str(self.price[i]*self.quant[i]))
        print("\t\t\t\t\t\t",str(self.gt)+"\t"+str(self.dis)+"\t"+str(self.net))  
    
custlist=[]
for j in range(n):
    custlist.append(shoping())

for dr in custlist:
    dr.custread()
    dr.proread()

    
print("cname\tSr.NO\tProduct\tPrice\tQty\tTotal\tG TOtal\tDis\tNetPrice")

for ds in custlist:
    ds.custshow()
    ds.proshow()