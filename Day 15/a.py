def reverse_array(arr):
    left=0
    right=len(arr)-1

    while left < right:
        arr[left],arr [right]=arr[right],arr[left]
        left+=1
        right+=1
    return arr
    
original_array=[10,2,3,4,5]
print("Original:",original_array)
reversed_array=reverse_array(original_array)
print("Reversed:",reversed_array)



