'''Create a function that finds the second smallest element in a list.'''

def second_smallest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()
    return unique_lst[1] if len(unique_lst) > 1 else None

# Example usage
lst = [10, 20, 4, 45, 99, 4]
print(f"Second smallest element: {second_smallest(lst)}")
