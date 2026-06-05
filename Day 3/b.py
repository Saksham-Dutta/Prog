# Write a program to Print prime numbers in a range.
n = int(input("Enter a number: ")) # 21
for i in range(2,  n + 1 ): # 2,3,4,5,6,7,8,.......21 (inclusive)
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            # break
    if isPrime:
        print(i)
