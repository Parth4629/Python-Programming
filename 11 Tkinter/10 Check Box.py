from tkinter import *   
  
top = Tk()  
  
top.geometry("300x300")  
  
checkvar1 = IntVar() 
  
checkvar2 = IntVar()  
  
checkvar3 = IntVar()  
  
chkbtn1 = Checkbutton(top, text ="C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn2 = Checkbutton(top, text ="C++", variable = checkvar2, onvalue = 2, offvalue = 0, height = 2, width = 10)  
  
chkbtn3 = Checkbutton(top, text ="Java", variable = checkvar3, onvalue = 3, offvalue = 0, height = 2, width = 10)  
  
chkbtn1.pack()  
  
chkbtn2.pack()  
  
chkbtn3.pack()


def btnclick():
    
    if checkvar1.get()==1:
        lt1.config(text="C")

    if checkvar2.get()==2:
        lt1.config(text="C++")

    if checkvar3.get()==3:
        lt1.config(text="Java")

    if checkvar1.get()==1 and checkvar2.get()==2:
        lt1.config(text="C,C++")
    
    if checkvar1.get()==1 and checkvar3.get()==3:
        lt1.config(text="C,Java")

    if checkvar2.get()==2 and checkvar3.get()==3:
        lt1.config(text="C++,Java")

    if checkvar1.get()==1 and checkvar2.get()==2 and checkvar3.get()==3:
        lt1.config(text="C,C++,Java")
    
    
btn1=Button(top,text="Click",command=btnclick)
btn1.place(x=130,y=120)

l2 = Label(top,text="Ans:-")
l2.place(x=100,y=150)
lt1=Label(top)
lt1.place(x=130,y=150)
  
top.mainloop()  
