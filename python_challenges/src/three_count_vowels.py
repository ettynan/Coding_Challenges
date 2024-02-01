'''Write a function to count the number of vowels in a given string'''
import re

def count_vowels(str):
    vowels = re.findall(r"[aeiouAEIOU]", str)
    count = (len(vowels))
    return count

user_input = input("Write a word to get the number of vowels: ")
print(count_vowels(user_input))