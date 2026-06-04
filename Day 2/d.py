number = input("Enter your number: ").lower().strip()

if number == number[::-1]:
    print("This number is a palindrome.")
else:
    print("This number is not a palindrome.")
