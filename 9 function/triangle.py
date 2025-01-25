a=int(input("Enter The value a : "))


def triangle(a):

    for i in range (1,a+1):
        for k in range(1,a-i+1):
            print("  ",end="")
        for j in range (1,i+1):
            print("* ",end="  ")
        print("")

triangle(a)

