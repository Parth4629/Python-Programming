a=int(input("Enter The value : "))

def Armstrong(a):
    i=0
    b=a
    while(a>0):
        t=a%10
        i=i+t*t*t
        a=a//10
    if (i==b):
        print("This Number is Armstrong")
    else :
        print("This Number Not Armstrong")

Armstrong(a)