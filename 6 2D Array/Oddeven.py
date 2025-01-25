R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

for i in range(R):
	a = []
	for j in range(C):
		a.append(int(input("enter value :")))
	matrix.append(a)
	
print("\nOdd Array :")
for i in range(R):
	for j in range(C):
		if(matrix[i][j]%2==1):
		   print(matrix[i][j], end = " ")

print("\nEven Array :")
for i in range(R):
	for j in range(C):
		if(matrix[i][j]%2==0):
		   print(matrix[i][j], end = " ")



	