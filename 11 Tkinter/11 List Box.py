from tkinter import*

Frame = Tk()
Frame.geometry("600x300")

a1=Listbox(Frame)
a1.place(x=50,y=50)

a1.insert(1,"c++")  
a1.insert(2,"Android")
a1.insert(3,"Java")
a1.insert(4,"Python")  
a1.insert(5,".Net")

def btnclk1():
    a2.insert(END,a1.get(ACTIVE))
    a1.delete(ANCHOR)
     
def btnclk2():
    a1.insert(END,a2.get(ACTIVE))
    a2.delete(ANCHOR)

def btnclk3():
    for i in range(a1.size()):
        a2.insert(END,a1.get(i))
    for i in range(a1.size()):
        a1.delete(0,END)
def btnclk4():
    for i in range(a2.size()):
        a1.insert(END,a2.get(i))
    a2.delete(0,END)

b1=Button(Frame,text=">",command=btnclk1)
b1.place(x=290,y=50)

b2=Button(Frame,text="<",command=btnclk2)
b2.place(x=290,y=90)

b3=Button(Frame,text=">>",command=btnclk3)
b3.place(x=290,y=130)

b4=Button(Frame,text="<<",command=btnclk4)
b4.place(x=290,y=170)

a2=Listbox(Frame)
a2.place(x=430,y=50)
Frame.mainloop()