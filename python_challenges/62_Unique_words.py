'''Find Unique Words in an Array Containing Anagrams'''

from collections import Counter

def find_unique_words(words):
    '''Takes in a list of words and returns the unique words '''
    # Dictionary to store the canonical form as the key and the original words as values
    canonical_map = {}
    
    for word in words:
        # Create the canonical form by sorting the word
        sorted_word = ''.join(sorted(word))
        # Add the word to its canonical group
        if sorted_word in canonical_map:
            canonical_map[sorted_word].append(word)
        else:
            canonical_map[sorted_word] = [word]

    # Retrieve all words that are unique within their canonical group
    unique_words = []
    for group in canonical_map.values():
        if len(group) == 1:  # Only one word in this group
            unique_words.append(group[0])
    
    return unique_words

# Example
words = ["ear", "era", "are", "tea", "eat", "tan", "nat"]
print(find_unique_words(words))


# def find_unique_anagrams(words):
#     anagram_groups = {}

#     # Group words by their canonical form (sorted version of the word)
#     for word in words:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word not in anagram_groups:
#             anagram_groups[sorted_word] = word  # Add the first word found in the group

#     # Return the unique anagrams
#     return list(anagram_groups.values())

# # Example usage
# words = ["ear", "era", "are", "tea", "eat", "tan", "nat"]
# print(find_unique_anagrams(words))
