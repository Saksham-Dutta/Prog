def is_symmetric(matrix):
    rows=len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    if rows!=cols:
        return False
    for i in range(rows):
        for j in range(i+1,cols):
            if matrix[i][j] != matrix[j][i]:
                return False
            return True
        matrix_A = [
    [1, 7, 3],
    [7, 4, -5],
    [3, -5, 6]
]

print("Is Matrix A symmetric?", is_symmetric(matrix_A))