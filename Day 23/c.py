def is_anagram(str1, str2):
     
    clean_str1 = str1.replace(" ", "").lower()
    clean_str2 = str2.replace(" ", "").lower()
      
    if len(clean_str1) != len(clean_str2):
        return False
        
     
    return sorted(clean_str1) == sorted(clean_str2)

 
string_a = "Listen"
string_b = "Silent"

if is_anagram(string_a, string_b):
    print(f"'{string_a}' and '{string_b}' are anagrams!")
else:
    print(f"'{string_a}' and '{string_b}' are NOT anagrams.")