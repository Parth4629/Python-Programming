R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

for i in range(R):
	a = []
	for j in range(C):
		a.append(int(input("enter value :")))
	matrix.append(a)
	
max=matrix[0][0]
min=matrix[0][0]



for i in range(R):
	for j in range(C):
		if(matrix[i][j]>max):
			max=matrix[i][j]
		elif(matrix[i][j]<min):
			max=matrix[i][j]
		   
print("\nMinimum",min)
print("Maximum",max)
		   