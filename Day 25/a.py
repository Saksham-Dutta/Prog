def merge_sorted_arrays(arr1,arr2):
    i=0
    j=0
    merged=[]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            while i < len(arr1):
               merged.append(arr1[i])
               i += 1
            while j < len(arr2):
              merged.append(arr2[j])
              j += 1
if __name__ == "__main__":
    array_a = [1, 3, 5, 7]
    array_b = [2, 4, 6, 8, 9, 10]

    result = merge_sorted_arrays(array_a, array_b)
    print(f"Array 1: {array_a}")
    print(f"Array 2: {array_b}")
    print(f"Merged : {result}")