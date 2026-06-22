def reverse_array(arr,start,end):
    while start<end:
        arr[start],arr[end]= arr[end],arr[start]
        start+=1
        end-=1
def rotate_right(arr,d):
    n=len(arr)
    if n==0:
        return arr
    d=d % n
    reverse_array(arr,0,n-1)
    reverse_array(arr,0,d-1)
    reverse_array(arr,d,n-1)
    return arr

if __name__ == "__main__":
    my_array = [1, 2, 3, 4, 5, 6, 7]
    positions_to_rotate = 3
    
    print("Original Array:", my_array)
    rotate_right(my_array, positions_to_rotate)
    print(f"Rotated Right by {positions_to_rotate}:", my_array)
    
