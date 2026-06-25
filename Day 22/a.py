def is_palindrome(text):
    
    clean_text = text.lower()
    return clean_text == clean_text[::-1]
 
word1 = "Radar"
word2 = "Python"

print(f"Is '{word1}' a palindrome? {is_palindrome(word1)}")  # Output: True
print(f"Is '{word2}' a palindrome? {is_palindrome(word2)}")  # Output: False