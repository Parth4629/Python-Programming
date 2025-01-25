a=int(input("Enter Value a :"))
b=int(input("Enter Value b :"))

for i in range(a,b+1):
    for j in range (1,11):
        result =i*j
        print(i ,'x', j, '=' ,result)
