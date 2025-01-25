from tkinter import *
Frame = Tk()
Frame.geometry("500x450")
l1 = Label(Frame,text="Enter Value 1: ").place(x=30,y=50)
l2 = Label(Frame,text="Enter Value 2: ").place(x=30,y=90)

e1=Entry(Frame)
e1.place(x=120,y=50)
e2=Entry(Frame)
e2.place(x=120,y=90)


def btnclk():
    total=int(e1.get())+int(e2.get())
    lt.configure(text=str(total))

def btnclk1():
    total1=int(e1.get())-int(e2.get())
    lt.configure(text=str(total1))

def btnclk2():
    total2=int(e1.get())/int(e2.get())
    lt.configure(text=str(total2))

def btnclk3():
    total3=int(e1.get())*int(e2.get())
    lt.configure(text=str(total3))

    
b1=Button(Frame,text="sum",command=btnclk)   
b1.place(x=100,y=120)

b2=Button(Frame,text="Sub",command=btnclk1)
b2.place(x=140,y=120)

b3=Button(Frame,text="Div",command=btnclk2)
b3.place(x=180,y=120)

b4=Button(Frame,text="Mul",command=btnclk3)
b4.place(x=220,y=120)
  

lrt = Label(Frame, text = "Result:")
lrt.place(x=30, y=200)  
lt = Label(Frame)
lt.place(x=120, y=200)  

Frame.mainloop()