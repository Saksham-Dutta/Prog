def find_frequency(arr,target):
    count=0
    for element in arr:
        if element == target:
            count+=1
    return count
my_list=[10,20,30,20,50,20,40]
target_val=20
result= find_frequency(my_list,target_val)
print(f"the element {target_val} appears {result} times.")