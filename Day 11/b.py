def find_max(a,b):
    if a>b:
        return a
    if b<a:
        return b
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
maximum=find_max(num1,num2)
print("Maximum number is:",maximum)
