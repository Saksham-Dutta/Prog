# Write a program to Check whether a number is prime.

a = int(input("Enter a number: "))

isPrime = True

for i in range(2, a):
    if a % i == 0:
        isPrime = False
        break

if isPrime:
    print("Prime number.")
else:
    print("Not a prime number.")