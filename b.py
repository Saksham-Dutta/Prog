from collections import Counter
def find_common_characters(strings):
    if not strings:
        return []
    common_counts = Counter(strings[0])
    next_counts = Counter(next_string)

    for char in list(common_counts.keys()):
            if char in next_counts:
                common_counts[char] = min(common_counts[char], next_counts[char])
            else:
                del common_counts[char]
    result = []
    for char, count in common_counts.items():
        result.extend([char] * count)

    return result
if __name__ == "__main__":
    words = ["bella", "label", "roller"]
    print(f"Input:  {words}")
    print(f"Output: {find_common_characters(words)}")