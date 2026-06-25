def first_repeating_char(text):
    seen = set()
    
    for char in text:
        if char in seen:
            return char   
        seen.add(char)    
        
    return None   

# Example usage:
print(first_repeating_char("swiss"))             
print(first_repeating_char("python"))            
print(first_repeating_char("abcdefgfedcba"))    