def subtract_matrices(mat1, mat2):
    # Check if matrices have the same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions")

    # Create a new matrix filled with 0s to store the result
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]

    # Perform subtraction
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] - mat2[i][j]

    return result

# Example usage
A = [[5, 6, 7],
     [8, 9, 10]]

B = [[1, 2, 3],
     [4, 5, 6]]

diff = subtract_matrices(A, B)

for row in diff:
    print(row)