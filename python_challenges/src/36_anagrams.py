'''Write a Python program to check if two strings are anagrams'''

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage
print(f"Are 'listen' and 'silent' anagrams? {are_anagrams('listen', 'silent')}")
