def first_non_repeating_char_dict(text):
    char_counts = {}
    
    
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
         
    for char in text:
        if char_counts[char] == 1:
            return char
            
    return None

# Example usage:
print(first_non_repeating_char_dict("pythonprogramming"))