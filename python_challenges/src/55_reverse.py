'''Create a function that takes a string and returns the reverse of each word'''

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Example usage
sentence = "Hello world"
print(f"Reversed words: {reverse_words(sentence)}")
