matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

 
transposed = list(map(list, zip(*matrix)))

print("Original Matrix:", matrix)
print("Transposed Matrix:", transposed)
 