n = int(input("Enter a number: "))
print(f"\nMultiplication Table of {n}")
print("-" * 20)
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
