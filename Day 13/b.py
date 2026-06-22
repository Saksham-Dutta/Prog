def find_sum_and_average(arr):
    if not arr:
        return 0, 0
        
    total_sum = sum(arr)
    average = total_sum / len(arr)
    
    return total_sum, average

 
numbers = [10, 20, 30, 40, 50]
total, avg = find_sum_and_average(numbers)

print(f"Array: {numbers}")
print(f"Sum: {total}")
print(f"Average: {avg}")