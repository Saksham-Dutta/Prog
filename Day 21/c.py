def count_vowels_and_consonants(text):
    vowels = set("aeiou")
    
    vowel_count = 0
    consonant_count = 0
    
    
    for char in text.lower():
        if char.isalpha():   
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count

# Example usage:
input_string = "Hello, World! 2026"
vowels_num, consonants_num = count_vowels_and_consonants(input_string)

print(f"String: '{input_string}'")
print(f"Vowels: {vowels_num}")
print(f"Consonants: {consonants_num}")
