num = int(input("Enter a number: "))

largest_factor = 1
n = num

i=2

while i * i <= n:
    while n % i==0:
        largest_factor = i
        n = n //i
    i += 1

if n > 1:
    largest_factor = n

print("Largest prime factor:",largest_factor)
        

        
        


