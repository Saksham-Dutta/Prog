def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None
        
    
    largest = numbers[0]
    smallest = numbers[0]
    
     
    for num in numbers:   
       if num>largest:
          largest=num
       if num<smallest:
           smallest=num
           

            
    return largest, smallest

 
nums = [34, 12, 89, 5, 47, 92, 21]
max_val, min_val = find_largest_and_smallest(nums)
print(f"Largest element: {max_val}")
print(f"Smallest element: {min_val}")

