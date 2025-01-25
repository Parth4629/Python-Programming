a=int(input("start Value : "))
b=int(input("start Value : "))

def mmt(a):
    for i in range(a,b+1):
        for j in range(1,11):
            result=i*j
            print(i,'x',j,'=',result)
            
mmt(a)
