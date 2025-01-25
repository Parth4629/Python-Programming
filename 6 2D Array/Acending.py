R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the matrix rowwise:")

for i in range(R):
	a = []
	for j in range(C):
		a.append(int(input("enter value :")))
	matrix.append(a)
	

for i in range(R):
	for j in range(C):
		for k in range(j+1,C):
		    
			if (matrix[i][j]>matrix[i][k]):
				trmp=matrix[i][j]
				matrix[i][j]=matrix[i][k]
				matrix[i][k]=trmp

print("\nAcending :")
for i in range(R):
	for j in range(C):
		print(matrix[i][j])
	print("")


for i in range(R):
	for j in range(C):
		for k in range(j+1,C):
		    
			if (matrix[i][j]<matrix[i][k]):
				trmp=matrix[i][j]
				matrix[i][j]=matrix[i][k]
				matrix[i][k]=trmp

print("\nDecending :")
for i in range(R):
	for j in range(C):
		print(matrix[i][j])
	print("")

