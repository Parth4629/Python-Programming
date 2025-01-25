od=""
for i in range(1,101):
    if(i%2==1):
     
        od=od+str(i)+","

    
f=open("odd value.txt","w")

f.write(od)
        
f.close()


ed=""
for j in range(1,101):
    if(j%2==0):
        ed=ed+str(j)+","



d=open("Even Value.txt","w")
d.write(ed)

d.close()


print("file successfully created...")




