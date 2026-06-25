def add_matrices(matrix1,matrix2):
    rows=len(matrix1)
    cols=len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
     for j in range(cols):
         result[i][j] = matrix1[i][j] + matrix2[i][j]

     return result

 
matrix_A = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_B = [
    [7, 8, 9],
    [1, 2, 3]
]
sum_matrix=add_matrices(matrix_A,matrix_B)
print("Resultant matrix")
for row in sum_matrix:
   print(row)
   
 