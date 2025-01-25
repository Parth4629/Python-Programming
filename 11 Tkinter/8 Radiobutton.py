from tkinter import *

frame = Tk()
frame.geometry('300x200')


radio = IntVar()
rm = Radiobutton(frame,text='male',variable=radio,value=1)
rm.place(x=20,y=20)
rf = Radiobutton(frame,text='female',variable=radio,value=2)
rf.place(x=80,y=20)

def btnClk():
    if radio.get()==1:
        lt1.configure(text="Male")
    elif radio.get()==2:
        lt1.config(text="Female")
    else:
        lt1.config(text="pls select gender")

btn1 = Button(frame,text='submit',command=btnClk)
btn1.place(x=20,y=60)


lt1 = Label(frame)
lt1.place(x=80,y=60)

frame.mainloop()