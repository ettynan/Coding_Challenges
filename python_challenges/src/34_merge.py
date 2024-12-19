'''Write a Python program to merge two dictionaries'''

# The ** operator is used to unpack the key-value pairs of each dictionary. This syntax takes the keys and values from dict1 and dict2 and combines them into a single dictionary.
# If both dictionaries contain the same key, the value from dict2 will overwrite the value from dict1 because dict2 is unpacked last.
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(f"Merged dictionary: {merge_dicts(dict1, dict2)}")
