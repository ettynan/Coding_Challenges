'''Write a program to remove vowels from a given string'''

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])

# Example usage
s = "hello world"
print(f"String without vowels: {remove_vowels(s)}")
