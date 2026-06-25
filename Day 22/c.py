def character_frequency(text):
    frequency = {}
    
    for char in text:
        
        if char in frequency:
            frequency[char] += 1
         
        else:
            frequency[char] = 1
            
    return frequency

 
text_input = "hello"
print(character_frequency(text_input))
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}