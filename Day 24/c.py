def find_longest_word(sentence):
    words= sentence.split()
    if not words:
        return "No words found"
        return max(words, key=len)
text = "Python programming is incredibly powerful and versatile"
longest = find_longest_word(text)

print(f"The longest word is: {longest}")
print(f"Its length is: {len(longest)}")
    