# Write a program to Find GCD of two numbers
def returnFactorSet(num):
    factors = set()
    for i in range(1, num + 1):
        if num % i == 0:
            factors.add(i)
    return factors

numOne = int(input("Enter 1st number: "))
numTwo = int(input("Enter 2nd number: "))

factorsOfNumOne = returnFactorSet(numOne)
factorsOfNumTwo = returnFactorSet(numTwo)

print(f"GCD: {max(factorsOfNumOne.intersection(factorsOfNumTwo))}")
