'''Write a program to remove duplicates from a list'''

def remove_duplicates(lst):
    return list(set(lst))

# Example usage
lst = [1, 2, 2, 3, 4, 4, 5]
print(f"List without duplicates: {remove_duplicates(lst)}")
