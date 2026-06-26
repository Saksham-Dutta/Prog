def compress_string(s: str) -> str:
    if not s:
        return ""

    compressed = []
    current_char = s[0]
    count = 1

 
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
 
    compressed.append(f"{current_char}{count}")
 
    compressed_str = "".join(compressed)

    
    return compressed_str if len(compressed_str) < len(s) else s

 
if __name__ == "__main__":
    test1 = "aabcccccaaa"
    test2 = "abcdef"
    test3 = "aaaaaa"

    print(f"Original: {test1:15} -> Compressed: {compress_string(test1)}")
    print(f"Original: {test2:15} -> Compressed: {compress_string(test2)}")
    print(f"Original: {test3:15} -> Compressed: {compress_string(test3)}")