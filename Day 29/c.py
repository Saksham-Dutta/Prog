def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    # Removing spaces and converting to lowercase for an accurate check
    cleaned = "".join(s.split()).lower()
    return cleaned == cleaned[::-1]

def string_operations():
    # Get the initial string from the user
    user_string = input("Enter a string to work with: ")

    while True:
        print("\n--- String Operations Menu ---")
        print(f"Current String: \"{user_string}\"")
        print("1. Reverse the string")
        print("2. Count vowels")
        print("3. Check if Palindrome")
        print("4. Convert to Uppercase")
        print("5. Enter a new string")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            print(f"Reversed String: {reverse_string(user_string)}")
            
        elif choice == '2':
            print(f"Number of Vowels: {count_vowels(user_string)}")
            
        elif choice == '3':
            if is_palindrome(user_string):
                print("Result: Yes, it is a palindrome!")
            else:
                print("Result: No, it is not a palindrome.")
                
        elif choice == '4':
            print(f"Uppercase: {user_string.upper()}")
            
        elif choice == '5':
            user_string = input("Enter new string: ")
            print("String updated successfully.")
            
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 6.")

if __name__ == "__main__":
    string_operations()