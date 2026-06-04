# Q8	Write a program to Check whether a number is palindrome.
number = input("Enter your number: ").lower().strip()

if number == number[::-1]:
    print("This number is a palindrome.")
else:
    print("This number is not a palindrome.")
