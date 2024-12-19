'''Write a program to shuffle the elements of a list randomly'''

import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

# Example usage
lst = [1, 2, 3, 4, 5]
print(f"Shuffled list: {shuffle_list(lst)}")
