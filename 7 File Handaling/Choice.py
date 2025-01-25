a=input("Enter The File Name : ")

print("(1) C Language niven.c")
print("(2) C++ Niven.cpp")
print("(3) java Niven.java")
print("(4) Python Niven.py")

b=int(input("Enter your Choice : "))

if b==1:
    f=open(a+".c","w")
    f.write("#include<stdio.h>")
    f.close()

if b==2:
    f=open(a+".c++","w")
    f.write("#include<stdio.h>")
    f.close()
if b==3:
    f=open(a+".java","w")
    f.write("import.java.until")
    f.close()

if b==4:
    f=open(a+".py","w")
    f.write("print("")")
    f.close()

print("file successfully created...")
