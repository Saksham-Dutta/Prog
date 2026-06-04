# Q7\tWrite a program to Find product of digits.

s = input("Enter your number: ")

digits = [ch for ch in s]

result = 1
for d in digits:
    result *= int(d)
print(f"Result of product of digits of {''.join(digits)}: {result}")
