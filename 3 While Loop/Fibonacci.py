a=int(input("Enter The Value a: "))
t1=1
t2=0
i=0
while (i<a):
    i=i+1
    t3=t1+t2
    t1=t2
    t2=t3
    print(t1,end=",")
