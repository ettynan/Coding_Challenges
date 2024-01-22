'''You are given two strings word1 and word2. Merge the strings by adding letters
in alternating order, starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.
Return the merged string.'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # split each word?
        # or just take word[i] and loop thru both
        # for l in letters in range(len(word1)):
        string_merged = ""
        i = 0
        while (i < len(word1)) or (i < len(word2)):
            if i < len(word1):
                string_merged += word1[i]
            if i < len(word2):
                string_merged += word2[i]
            i+=1
        return string_merged