'''Write a program that checks if a key exists in a dictionary'''

def check_key_in_dict(my_dict, key):
    return key in my_dict

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
print(f"Does the key '{key}' exist in the dictionary? {check_key_in_dict(my_dict, key)}")
