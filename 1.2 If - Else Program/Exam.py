r=w=at=ut=0

print("************ Online Exam *************")

print("Que-1: 5*2=?")
print("(1) 25")
print("(2) 10")
print("(3) 09")
print("(4) Skip")

ch=input("Enter your option =")

if ch==4:
    ut=ut+1
     
elif ch==2:
    r=r+1
    at=at+1
else:
    w=w+1
    at=at+1


print("Que-2: 5*2-2=?")
print("(1) 8")
print("(2) 9")
print("(3) 10")
print("(4) Skip")

ch=input("Enter your option =")

if ch==4:
    ut=ut+1
     
elif ch==1:
    r=r+1
    at=at+1
else :
    w=w+1
    at=at+1
       

print("Que-3: 75*2=?")
print("(1) 180")
print("(2) 150")
print("(3) 100")
print("(4) Skip")

ch=input("Enter your option =")

if ch==4:
    ut=ut+1
     
elif ch==2:
    r=r+1
    at=at+1
else :
    w=w+1
    at=at+1


print("Que-4: 55+20=?")
print("(1) 85")
print("(2) 90")
print("(3) 75")
print("(4) Skip")

ch=input("Enter your option =")

if ch==4:
    ut=ut+1
     
elif ch==3:
    r=r+1
    at=at+1
else :
    w=w+1
    at=at+1


print("Que-5: 5+2+6+7=?")
print("(1) 20")
print("(2) 19")
print("(3) 21")
print("(4) Skip")

ch=input("Enter your option =")

if ch==4:
    ut=ut+1
     
elif ch==1:
    r=r+1
    at=at+1
else :
    w=w+1
    at=at+1
            
    
print("Attend ans=",at)
print("UnAttend ans=",ut)
print("Right ans",r)
print("Wrong Ans",w)