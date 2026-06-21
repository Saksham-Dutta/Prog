def is_armstrong_str(num):
    num_str=str (num)
    num_digits=len(num_str)
    total_sum=sum(int(digit)** num_digits for digit in num_str)
    return total_sum==num
print(is_armstrong_str(153))    
print(is_armstrong_str(9474))    
print(is_armstrong_str(123))