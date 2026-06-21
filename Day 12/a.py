def is_palindrome(text):
    clean_text =str(text).lower() 
    return clean_text==clean_text[::-1]
print(is_palindrome("radar"))
print(is_palindrome("Hello"))
print(is_palindrome(12321))