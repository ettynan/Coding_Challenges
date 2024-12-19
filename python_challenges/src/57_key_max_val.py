'''Create a function that returns the key with the maximum value in a dictionary'''

def max_value_key(d):
    return max(d, key=d.get)

# Example usage
sample_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"Key with the maximum value: {max_value_key(sample_dict)}")
