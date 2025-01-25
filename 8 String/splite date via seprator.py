#split date via multiple seprator

a=(input("Enter The date : ")) 

b = a.replace('-',',').replace('/',',').replace(' ',',').replace('.',',').split(',')
        
print("\nDays = ",b[0])
print("Months = ",b[1])
print("Years = ",b[2])
  