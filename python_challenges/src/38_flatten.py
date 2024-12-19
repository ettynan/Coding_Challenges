'''Write a program to flatten a nested list'''

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

# Example usage
nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"Flattened list: {flatten_list(nested)}")
