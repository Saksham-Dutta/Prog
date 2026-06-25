matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# zip(*matrix) groups elements by columns, then sum() adds them up
col_sums = [sum(col) for col in zip(*matrix)]

print("Column-wise sums:", col_sums)