'''Write a function that counts th frequency of each word in a sentence'''

from collections import Counter

def word_frequency(sentence):
    words = sentence.split()
    return dict(Counter(words))

# Example usage
sentence = "hello world hello python"
print(f"Word frequency: {word_frequency(sentence)}")
