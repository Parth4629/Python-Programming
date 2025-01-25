import mysql.connector

con=mysql.connector.connect(host="localhost", user="root", password="", database="dharadb")

cmd=con.cursor()



name=input("enter the name:")
email=input("enter the email:")
password=input("enter the password:")
mobile=input("enter the mobile:")
cmd.execute("insert into registration values(NULL,%s,%s,%s,%s)",(name,email,password,mobile))
con.commit()
print("your data successfully saved...")
con.close()