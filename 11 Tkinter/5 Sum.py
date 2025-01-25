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
  
b5=Button(Frame,text="Submit",command=btnclk)
b5.place(x=120,y=160)


lrt = Label(Frame, text = "Result:")
lrt.place(x=30, y=200)  
lt = Label(Frame)
lt.place(x=120, y=200)  

Frame.mainloop()