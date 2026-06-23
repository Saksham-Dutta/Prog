def find_pair_with_sum(arr,target_sum):
    seen=set()
    for num in arr:
        complement= target_sum-num
        if complement in seen:
            return(complement,num)
        seen .add(num)
        return None
    numbers = [3, 5, 2, 8, 11, 7]
target = 10

pair = find_pair_with_sum(numbers, target)
print(f"Pair found: {pair}")

 
     