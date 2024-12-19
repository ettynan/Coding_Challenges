from collections import Counter

def top_10_frequent_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    word_counts = Counter(words)
    return word_counts.most_common(10)

# Example usage:
# Save "large_text.txt" in the same directory for this to work
# print(top_10_frequent_words("large_text.txt"))
