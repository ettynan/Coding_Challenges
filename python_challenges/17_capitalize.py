'''Create a program that capitalizes the first letter of each word in a sentence'''

def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

# Example usage
sentence = "hello world from python"
print(f"Capitalized sentence: {capitalize_words(sentence)}")
