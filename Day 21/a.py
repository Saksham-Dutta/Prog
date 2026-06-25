def find_length_short(string):
    # Generates a 1 for every character in the string, then sums them
    return sum(1 for char in string)

# Test the function
text = "OpenAI"
print(f"The length of '{text}' is: {find_length_short(text)}")
