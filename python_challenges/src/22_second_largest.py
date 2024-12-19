'''Create a program to find the second-largest element in a list.'''

def second_largest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

# Example usage
lst = [10, 20, 4, 45, 99, 20]
print(f"Second largest element: {second_largest(lst)}")
