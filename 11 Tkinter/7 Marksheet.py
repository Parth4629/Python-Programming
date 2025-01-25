from tkinter import *
Frame = Tk()
Frame.geometry("500x500") 
l1 =   Label(Frame,text="Enter Marks 1: ").place(x=30,y=50)
l2 =   Label(Frame,text="Enter Marks 2: ").place(x=30,y=90)
l3 =   Label(Frame,text="Enter Marks 3: ").place(x=30,y=130)
l4 =   Label(Frame,text="Enter Marks 4: ").place(x=30,y=170)
l5 =   Label(Frame,text="Enter Marks 5: ").place(x=30,y=210)

e1=Entry(Frame)
e1.place(x=120,y=50)

e2=Entry(Frame)
e2.place(x=120,y=90)

e3=Entry(Frame)
e3.place(x=120,y=130)

e4=Entry(Frame)
e4.place(x=120,y=170)

e5=Entry(Frame)
e5.place(x=120,y=210)


def btnclk():
    total=int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())+int(e5.get())
    lt1.configure(text=str(total))

    percentage=total/5
    lt2.configure(text=str(percentage))

    if percentage>90:
        lt3.configure(text=str("Grade A+"))

    elif percentage>75:
        lt3.configure(text=str("Grade A"))

    elif percentage>60:
        lt3.configure(text=str("Grade B")) 

    elif percentage>45:
        lt3.configure(text=str("Grade C"))

    elif percentage>35:
        lt3.configure(text=str("Grade D"))
    
    else:
        lt3.configure(text=str("Fail"))

def btnclear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    lt1.configure(text="")
    lt2.configure(text="")
    lt3.configure(text="")

def btnexit():
    exit()

#button

b1=Button(Frame,text="SUBMIT",command=btnclk)
b1.place(x=110,y=240)

b2=Button(Frame,text="CLEAR",command=btnclear)
b2.place(x=170,y=240)

b3=Button(Frame,text="EXIT",command=btnexit)
b3.place(x=230,y=240)

#label 1

lrt1=Label(Frame,text="Total:-")
lrt1.place(x=30,y=280)
lt1=Label(Frame)
lt1.place(x=120,y=280)

#label 2

lrt2=Label(Frame,text="Percentage:-")
lrt2.place(x=30,y=320)
lt2=Label(Frame)
lt2.place(x=120,y=320)

#label 3

lrt3=Label(Frame,text="Grade:-")
lrt3.place(x=30,y=360)
lt3=Label(Frame)
lt3.place(x=120,y=360)


Frame.mainloop()