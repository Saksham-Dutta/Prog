def intersect_arrays(arr1,arr2):
    return list(set(arr1)& set(arr2))
 array1 = [1, 2, 2, 3, 4]
array2 = [2, 2, 4, 6, 7]

result = intersect_arrays(array1, array2)
print("Intersection:", result)