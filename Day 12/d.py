def is_perfect_number(num):
    # Perfect numbers must be positive integers greater than 1
    if num <= 1:
        return False
        
    divisor_sum = 1 # 1 is always a proper divisor
    
    # Check divisors up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            # If the paired divisor is different, add it too
            if i != num // i:
                divisor_sum += num // i
                
    return divisor_sum == num
print(is_perfect_number(6))    
print(is_perfect_number(28))    
print(is_perfect_number(496))  
print(is_perfect_number(12))