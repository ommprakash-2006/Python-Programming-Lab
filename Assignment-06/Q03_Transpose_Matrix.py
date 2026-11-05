Rows=int(input("Give the number of rows:"))
Columns=int(input("Give the number of columns:"))
matrix=[[int(input()) for c in range(Columns)] for r in range(Rows)]
print(Rows)
print("Original Matrix")
for i in range(0,Rows):
 for j in range(0,Columns): print(matrix[i][j],"\t",end=" ")
 print()
print("Matrix after transpose")
for i in range(0,Rows):
 for j in range(0,Columns): print(matrix[j][i],"\t",end="")
 print()