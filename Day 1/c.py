n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"Factorial of {n} is {factorial}")
