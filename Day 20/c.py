matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate through each row
for i in range(len(matrix)):
    current_row_sum = 0
    # Iterate through each element in the row
    for j in range(len(matrix[i])):
        current_row_sum += matrix[i][j]
        
    print(f"Sum of Row {i+1}: {current_row_sum}")