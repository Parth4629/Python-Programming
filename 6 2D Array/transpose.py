R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

for i in range(R):
	a = []
	for j in range(C):
		a.append(int(input("enter value :")))
	matrix.append(a)


print("\nOrignal Value: ")
for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()


for i in range (R):
	for j in range (C):
		temp=matrix[i][j]
		matrix[i][j]=matrix[j][i]
		matrix[j][i]=temp

print("\nTranspose Value: ")
for i in range(R):
	for j in range(C):
		print(matrix[j][i],end=" ")
	print()
     

