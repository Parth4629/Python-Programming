from tkinter import *

frame = Tk()
frame.geometry('600x600')
#radiobutton

l1 = Label(frame,text=("(1)24/2=?"))
l1.place(x=20,y=30)

radio1 = IntVar()

r1 = Radiobutton(frame,text='(a)12',variable=radio1,value=1)
r1.place(x=20,y=50)
r2 = Radiobutton(frame,text='(b)20',variable=radio1,value=2)
r2.place(x=80,y=50)
r3 = Radiobutton(frame,text='(c)33',variable=radio1,value=3)
r3.place(x=140,y=50)
r4 = Radiobutton(frame,text='(d)skip',variable=radio1,value=4)
r4.place(x=200,y=50)

l2 = Label(frame,text=("(2)12+8=?"))
l2.place(x=20,y=80)

radio2 = IntVar()

r1 = Radiobutton(frame,text='(a)22',variable=radio2,value=1)
r1.place(x=20,y=100)
r2 = Radiobutton(frame,text='(b)25',variable=radio2,value=2)
r2.place(x=80,y=100)
r3 = Radiobutton(frame,text='(c)20',variable=radio2,value=3)
r3.place(x=140,y=100)
r4 = Radiobutton(frame,text='(d)skip',variable=radio2,value=4)
r4.place(x=200,y=100)

l3 = Label(frame,text=("(3)12*2=?"))
l3.place(x=20,y=130)

radio3 = IntVar()

r1 = Radiobutton(frame,text='(a)26',variable=radio3,value=1)
r1.place(x=20,y=150)
r2 = Radiobutton(frame,text='(b)24',variable=radio3,value=2)
r2.place(x=80,y=150)
r3 = Radiobutton(frame,text='(c)36',variable=radio3,value=3)
r3.place(x=140,y=150)
r4 = Radiobutton(frame,text='(d)skip',variable=radio3,value=4)
r4.place(x=200,y=150)

l4 = Label(frame,text=("(4)2*4+6=?"))
l4.place(x=20,y=180)

radio4 = IntVar()

r1 = Radiobutton(frame,text='(a)12',variable=radio4,value=1)
r1.place(x=20,y=200)
r2 = Radiobutton(frame,text='(b)20',variable=radio4,value=2)
r2.place(x=80,y=200)
r3 = Radiobutton(frame,text='(c)14',variable=radio4,value=3)
r3.place(x=140,y=200)
r4 = Radiobutton(frame,text='(d)skip',variable=radio4,value=4)
r4.place(x=200,y=200)


def btnsubmit():

    at=0
    un=0
    wr=0
    rt=0
    gt=0
    cu=0

    #quation1
    #write ans

    if radio1.get()==1:
        at=at+1
        rt=rt+1
        gt=gt+5

    #wrong ans

    elif radio1.get()==2 or radio1.get()==3:
        at=at+1
        wr=wr+1
        cu=cu-2
        
    #skip

    else:
        un=un+1
    t= gt+cu
    lt1.config(text=str(at))
    lt2.config(text=str(un))
    lt3.config(text=str(wr))
    lt4.config(text=str(rt))
    lt5.config(text=str(gt))
    lt6.config(text=str(cu))
    lt7.config(text=str(t))

    #quation2
    #write ans

    if radio2.get()==3:
        at=at+1
        rt=rt+1
        gt=gt+5

    #wrong ans

    elif radio2.get()==1 or radio2.get()==2:
        at=at+1
        wr=wr+1
        cu=cu-2
        
    #skip

    else:
        un=un+1
    t= gt+cu
    lt1.config(text=str(at))
    lt2.config(text=str(un))
    lt3.config(text=str(wr))
    lt4.config(text=str(rt))
    lt5.config(text=str(gt))
    lt6.config(text=str(cu))
    lt7.config(text=str(t))

    #quation3
    #write ans

    if radio3.get()==2:
        at=at+1
        rt=rt+1
        gt=gt+5

    #wrong ans

    elif radio3.get()==1 or radio3.get()==3:
        at=at+1
        wr=wr+1
        cu=cu-2
        
    #skip

    else:
        un=un+1
    t= gt+cu
    lt1.config(text=str(at))
    lt2.config(text=str(un))
    lt3.config(text=str(wr))
    lt4.config(text=str(rt))
    lt5.config(text=str(gt))
    lt6.config(text=str(cu))
    lt7.config(text=str(t))

    #quation4
    #write ans

    if radio4.get()==3:
        at=at+1
        rt=rt+1
        gt=gt+5

    #wrong ans

    elif radio4.get()==1 or radio4.get()==2:
        at=at+1
        wr=wr+1
        cu=cu-2
        
    #skip

    else:
        un=un+1
    t= gt+cu
    lt1.config(text=str(at))
    lt2.config(text=str(un))
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
    
    lt1.configure(text="")
    lt2.configure(text="")
    lt3.configure(text="")
    lt4.configure(text="")
    lt5.configure(text="")
    lt6.configure(text="")
    lt7.configure(text="")
    
    
def btnexit():
    exit()




# button
btn1 = Button(frame,text='submit',command=btnsubmit)
btn1.place(x=30,y=250)

btn2 = Button(frame,text='Clear',command=btnclear)
btn2.place(x=100,y=250)

btn3 = Button(frame,text='Exit',command=btnexit)
btn3.place(x=160,y=250)



#anser

lrt1 = Label(frame,text="attend:-")
lrt1.place(x=30,y=300)
lt1 = Label(frame)
lt1.place(x=120,y=300)

lrt2 = Label(frame,text="Unattend:-")
lrt2.place(x=30,y=330)
lt2 = Label(frame)
lt2.place(x=120,y=330)

lrt3 = Label(frame,text="Wrong Answe:-")
lrt3.place(x=30,y=360)
lt3 = Label(frame)
lt3.place(x=120,y=360)

lrt4 = Label(frame,text="Right answer:-")
lrt4.place(x=30,y=390)
lt4 = Label(frame)
lt4.place(x=120,y=390)

lrt5 = Label(frame,text="get marks:-")
lrt5.place(x=30,y=420)
lt5 = Label(frame)
lt5.place(x=120,y=420)

lrt6 = Label(frame,text="cut of marks:-")
lrt6.place(x=30,y=450)
lt6 = Label(frame)
lt6.place(x=120,y=450)

lrt7 = Label(frame,text="total marks:-")
lrt7.place(x=30,y=480)
lt7 = Label(frame)
lt7.place(x=120,y=480)
