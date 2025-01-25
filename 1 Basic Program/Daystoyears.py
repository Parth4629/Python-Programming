
a=int(input("Enter Days :"))


Years = a//365
Months = (a - Years*365)//30
Days = (a - Years*365 - Months*30)


print("Years = ", Years)
print("Months = ", Months)
print("Days = ", Days)


