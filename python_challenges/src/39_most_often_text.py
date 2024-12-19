'''Write a program to find the most common words in a text file'''

from collections import Counter
import re

def most_common_words(file_path):
    with open(file_path, 'r') as file:
        # The re.findall(r'\b\w+\b', ...) part will match the words "hello", "world", "this", "is", and "python", 
        # returning the list: ['hello', 'world', 'this', 'is', 'python']
        words = re.findall(r'\b\w+\b', file.read().lower())  # Read and process all text at once
    return Counter(words).most_common()

# Example usage
file_path = 'sample.txt'  # Replace with your text file path
for word, count in most_common_words(file_path):
    print(f"{word}: {count}")
