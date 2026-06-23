def find_missing_number(arr,n):
    expected_sum= n *(n+1)//2
    actual_sum=sum(arr)
    return expected_sum-actual_sum
numbers=[1,2,3,4,5,6]
n=6
missing=find_missing_number(numbers,n)
print(f"the missing number is:{missing}")

