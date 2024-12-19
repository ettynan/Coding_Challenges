'''Write a program to iterate through a dictionary and print its keys and values'''

def print_dict_keys_values(d):
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")

# Example usage
sample_dict = {'a': 1, 'b': 2, 'c': 3}
print_dict_keys_values(sample_dict)
