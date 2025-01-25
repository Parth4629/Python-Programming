from tkinter import*

frame = Tk()
frame.geometry("500x800")


#que 1

l1 = Label(frame,text="ONLINE EXAM").place(x=200,y=10)
l2 = Label(frame,text="Q.1-> 12+13 ?").place(x=40,y=30)

radio1 =IntVar()

a1=Radiobutton(frame,text="(a)21",variable=radio1,value=1)
a1.place(x=40,y=60)

a2=Radiobutton(frame,text="(b)25",variable=radio1,value=2)
a2.place(x=100,y=60)

a3=Radiobutton(frame,text="(c)27",variable=radio1,value=3)
a3.place(x=160,y=60)


#que=2

l3 = Label(frame,text="Q.2-> 5*12 ?").place(x=40,y=100)

radio2 =IntVar()

b1=Radiobutton(frame,text="(a)60",variable=radio2,value=1)
b1.place(x=40,y=130)

b2=Radiobutton(frame,text="(b)85",variable=radio2,value=2)
b2.place(x=100,y=130)

b3=Radiobutton(frame,text="(c)70",variable=radio2,value=3)
b3.place(x=160,y=130)


#que=3

l4 = Label(frame,text="Q.3-> 65-10+90 ?").place(x=40,y=170)

radio3 =IntVar()

c1=Radiobutton(frame,text="(a)145",variable=radio3,value=1)
c1.place(x=40,y=200)

c2=Radiobutton(frame,text="(b)155",variable=radio3,value=2)
c2.place(x=100,y=200)

c3=Radiobutton(frame,text="(c)135",variable=radio3,value=3)
c3.place(x=160,y=200)


#que=4


l5 = Label(frame,text="Q.4-> 128/8 ?").place(x=40,y=240)

radio4 =IntVar()

d1=Radiobutton(frame,text="(a)24",variable=radio4,value=1)
d1.place(x=40,y=270)

d2=Radiobutton(frame,text="(b)12",variable=radio4,value=2)
d2.place(x=100,y=270)

d3=Radiobutton(frame,text="(c)16",variable=radio4,value=3)
d3.place(x=160,y=270)


#que=5

l6 = Label(frame,text="Q.5-> x+12=35 Then x = ?").place(x=40,y=310)

radio5 =IntVar()

e1=Radiobutton(frame,text="(a)12",variable=radio5,value=1)
e1.place(x=40,y=340)

e2=Radiobutton(frame,text="(b)16",variable=radio5,value=2)
e2.place(x=100,y=340)

e3=Radiobutton(frame,text="(c)23",variable=radio5,value=3)
e3.place(x=160,y=340)


def btnsubmit():

    at=0
    ut=0
    wr=0
    rt=0
    gt=0
    cu=0

# Que - 1
# write Ans
    

    if radio1.get()==2:
        at=at+1
        rt=rt+1
        gt=gt+5

    elif radio1.get()==1 or radio1.get()==3:
        at=at+1
        wr=wr+1
        cu=cu-2

    else:
        ut=ut+1
    

# Que - 2

    if radio2.get()==1:
        at=at+1
        rt=rt+1
        gt=gt+5

    elif radio2.get()==2 or radio2.get()==3:
        at=at+1
        wr=wr+1
        cu=cu-2
    
    else:
        ut=ut+1
        

#Que - 3
        
    if radio3.get()==1:
        at=at+1
        rt=rt+1
        gt=gt+5

    elif radio3.get()==2 or radio3.get()==3:
        at=at+1
        wr=wr+1
        cu=cu-2
    
    else:
        ut=ut+1


#quation4

    if radio4.get()==3:
        at=at+1
        rt=rt+1
        gt=gt+5

    elif radio4.get()==1 or radio4.get()==2:
        at=at+1
        wr=wr+1
        cu=cu-2
    else:
        ut=ut+1



#quation 5

    if radio5.get()==3:
        at=at+1
        rt=rt+1
        gt=gt+5

    elif radio5.get()==1 or radio5.get()==2:
        at=at+1
        wr=wr+1
        cu=cu-2
    else:
        ut=ut+1
    t= gt+cu
    lt1.config(text=str(at))
    lt2.config(text=str(ut))
    lt3.config(text=str(wr))
    lt4.config(text=str(rt))
    lt5.config(text=str(gt))
    lt6.config(text=str(cu))
    lt7.config(text=str(t))



def btnclear():
    
    radio1.set(0)
    radio2.set(0)
    radio3.set(0)
    radio4.set(0)
    radio5.set(0)
    lt1.configure(text="")
    lt2.configure(text="")
    lt3.configure(text="")
    lt4.configure(text="")
    lt5.configure(text="")
    lt6.configure(text="")
    lt7.configure(text="")


def btnexit():
    exit()

#button

btn1=Button(frame,text="SUBMIT",command=btnsubmit)
btn1.place(x=40,y=380)

btn2=Button(frame,text="CLEAR",command=btnclear)
btn2.place(x=100,y=380)

btn3=Button(frame,text="EXIT",command=btnexit)
btn3.place(x=160,y=380)


#label 1

lrt1=Label(frame,text="Attend:-")
lrt1.place(x=40,y=410)
lt1=Label(frame)
lt1.place(x=120,y=410)

#label 2

lrt2=Label(frame,text="UnAttend:-")
lrt2.place(x=40,y=450)
lt2=Label(frame)
lt2.place(x=120,y=450)


#label 3

lrt3=Label(frame,text="Wrong Answer:-")
lrt3.place(x=40,y=500)
lt3=Label(frame)
lt3.place(x=120,y=500)


#label 4

lrt4=Label(frame,text="Right Answer:-")
lrt4.place(x=40,y=550)
lt4=Label(frame)
lt4.place(x=120,y=550)

#label 5

lrt5 = Label(frame,text="Get Marks:-")
lrt5.place(x=40,y=600)
lt5 = Label(frame)
lt5.place(x=120,y=600)

#label 6

lrt6 = Label(frame,text="Cut of Marks:-")
lrt6.place(x=40,y=650)
lt6 = Label(frame)
lt6.place(x=120,y=650)


#label 7

lrt7 = Label(frame,text="Total Marks:-")
lrt7.place(x=40,y=700)
lt7 = Label(frame)
lt7.place(x=120,y=700)

frame.mainloop()