'''Create a program that counts the occurrences of each word in a text file'''

import re
from collections import Counter

def count_word_occurrences(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()

        # Use regular expression to find words
        words = re.findall(r'\b\w+\b', content)
        
        # Count occurrences of each word
        word_counts = Counter(words)
        
        for word, count in word_counts.items():
            print(f"'{word}': {count} occurrences")

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")

# Example usage
count_word_occurrences("example.txt")
