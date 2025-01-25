from tkinter import *
import mysql.connector

Frame = Tk()
Frame.geometry("400x470")
l0 = Label(Frame,text="My BioData").place(x=150,y=10)
l1 = Label(Frame, text="Enter Name: ").place(x=30, y=50)
l2 = Label(Frame, text="Enter Email: ").place(x=30, y=90)
l3 = Label(Frame, text="Enter Password: ").place(x=30, y=130)
l4 = Label(Frame, text="Enter Mobile: ").place(x=30, y=170)

e1 = Entry(Frame)
e1.place(x=120, y=50)
e2 = Entry(Frame)
e2.place(x=120, y=90)
e3 = Entry(Frame)
e3.place(x=120, y=130)
e4 = Entry(Frame)
e4.place(x=120, y=170)

def Biodata():

    import mysql.connector

    con=mysql.connector.connect(host="localhost", user="root", password="", database="dharadb")

    cmd=con.cursor()

    cmd.execute("insert into registration values(Null,%s,%s,%s,%s)",(e1.get(),e2.get(),e3.get(),e4.get()))
    con.commit()
    print("your data successfully saved...")
    con.close()

def btnshow():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="dharadb")
        cmd = con.cursor()
        cmd.execute("SELECT * FROM registration")
        show = cmd.fetchall()
        data = ""
        for x in show:
            data += "%s\t%s\t%s\t%s\n" % (x[0], x[1], x[2], x[3])
        lt1.configure(text=data)
        con.close()
    except mysql.connector.Error as e:
        print("Error:", e)

def btnclear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    lt1.configure(text="")

btn1=Button(Frame,text="SUBMIT",command=Biodata)
btn1.place(x=100,y=200)    

btn2 = Button(Frame, text="SHOW", command=btnshow)
btn2.place(x=160, y=200)

btn3 = Button(Frame, text="CLEAR", command=btnclear)
btn3.place(x=220, y=200)

lt1 = Label(Frame)
lt1.place(x=140, y=250)

Frame.mainloop()