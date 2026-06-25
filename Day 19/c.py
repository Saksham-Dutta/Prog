matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# zip(*matrix) unpacks the rows and zips them column-wise
transpose = [list(x) for x in zip(*matrix)]

print("Transposed Matrix:")
for row in transpose:
    print(row)