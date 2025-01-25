a=int(input("Enter value: "))
def sigma(a):
    sum=0
    for i in range(1,a+1):
        sum=sum+i
        print(i,end=" + ")
    print("\nsum=",sum)

sigma(a)