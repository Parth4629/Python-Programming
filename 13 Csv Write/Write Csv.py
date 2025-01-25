import csv
with open('data.csv',"w") as csv_file:
    fieldnames=['First_Name','Last_Name','Rank']
    writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'First_Name':'janak','Last_Name':'suthar','Rank':'A'})
    writer.writerow({'First_Name':'Aditya','Last_Name':'Chauhan','Rank':'B'})
    writer.writerow({'First_Name':'Parth','Last_Name':'Patel','Rank':'C'})
    
print('done')