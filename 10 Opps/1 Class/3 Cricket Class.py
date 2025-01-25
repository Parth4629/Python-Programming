a=int(input("How many Cricketer data insert ? : "))

class Cricketers:

    def read(self):
        self.Cricketer=input("Enter Cricketer Name : ")
        self.Age=int(input("Enter Age : "))
        self.Country=input("Enter Country : ")
        self.Type=input("Enter Type Of Player : ")
        self.Run=int(input("Enter Total Run : "))
        self.Matches=int(input("Enter Total Matches : "))
        
    def show(self):
        print((self.Cricketer)+"\t\t"+str(self.Age)+"\t\t"+(self.Country)+"\t\t"+(self.Type)+"\t\t"+str(self.Run)+"\t\t"+str(self.Matches))

Cric=[]
for i in range(a):
    Cric.append(Cricketers())

for dr in Cric:
    dr.read()

print("\nCrickter\tAge\t\tCountry\t\tType\t\tRun\t\tMatches")

for ds in Cric:
    ds.show()