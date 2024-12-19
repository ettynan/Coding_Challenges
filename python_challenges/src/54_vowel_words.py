'''Create a function to find all words in a sentence that start with a vowel'''

def words_starting_with_vowel(sentence):
    vowels = "aeiou"
    words = sentence.split()
    return [word for word in words if word[0].lower() in vowels]

# Example usage
sentence = "An apple a day keeps the doctor away"
print(f"Words starting with a vowel: {words_starting_with_vowel(sentence)}")
