a=int(input("Enterthe value : "))
t=0

for i in range(1,a+1):
    t=t+1/i

    print("1/",i," + ",end="")
print("=",t)


