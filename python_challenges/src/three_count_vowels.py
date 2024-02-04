'''Write a function to count the number of vowels in a given string'''
import re

def count_vowels(str):
    vowels = re.findall(r"[aeiouAEIOU]", str)
    count = (len(vowels))
    return count

def get_user_input():
    """Prompts the user for a radius and handles potential input errors using a while loop."""
    while True:
        try:
            user_input = input("Write a word to get the number of vowels: ")
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    user_input = get_user_input()
    print(count_vowels(user_input))

