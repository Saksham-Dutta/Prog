def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
        return -1
my_list=[10,20,30,40,50]
target_val=30
result= linear_search( my_list,target_val)

if result!=-1:
    print(f"Element found at index:{result}")
else:
     print("Element not found.")