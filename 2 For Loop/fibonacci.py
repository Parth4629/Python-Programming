a=int(input("Enter The Value a: "))
t1=1
t2=0

for i in range (1,a+1):
    t3=t1+t2
    t1=t2
    t2=t3
    print(t1,end=",")
