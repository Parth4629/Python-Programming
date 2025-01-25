from tkinter import *

Frame = Tk()
Frame.geometry("600x300")

l1 = Label(Frame,text="Enter Name: ").place(x=30,y=50)
l2 = Label(Frame,text="Enter Email: ").place(x=30,y=90)
l3 = Label(Frame,text="Enter Password: ").place(x=30,y=130)
l4 = Label(Frame,text="Enter Mobile: ").place(x=30,y=170)

e1=Entry(Frame)
e1.place(x=120,y=50)
e2=Entry(Frame)
e2.place(x=120,y=90)
e3=Entry(Frame)
e3.place(x=120,y=130)
e4=Entry(Frame)
e4.place(x=120,y=170)

def Biodata():

    import mysql.connector

    con=mysql.connector.connect(host="localhost", user="root", password="", database="dharadb")

    cmd=con.cursor()

    cmd.execute("insert into registration values(Null,%s,%s,%s,%s)",(e1.get(),e2.get(),e3.get(),e4.get()))
    con.commit()
    print("your data successfully saved...")
    con.close()

btn1=Button(Frame,text="SUBMIT",command=Biodata)
btn1.place(x=100,y=220)
    
Frame.mainloop()