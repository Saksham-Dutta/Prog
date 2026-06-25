def count_words(sentence):
    words = sentence.split()
    return len(words)
sentence1 = "Python is fun to learn."
sentence2 = "  Too    many   spaces   here  "

print(f"Word count: {count_words(sentence1)}")   
print(f"Word count: {count_words(sentence2)}")   