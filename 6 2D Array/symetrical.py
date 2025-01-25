R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

for i in range(R):
	a = []
	for j in range(C):
		a.append(int(input("enter value :")))
	matrix.append(a)


print("\nOrignal Matrix: ")
for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()

flag=0

for i in range (R):
	for j in range (C):
		if (matrix[i][j]!=matrix[j][i]):
			flag=1
			

if (flag==0):
    print("\nThis is Symetrical Matrix: ")
else:
	print("\nThis not Symetrical Matrix: ")