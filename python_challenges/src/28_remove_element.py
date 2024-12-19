'''Create a program that removes the nth element from a list'''

def remove_nth_element(lst, n):
    if 0 <= n < len(lst):
        return lst[:n] + lst[n+1:]
    return lst

# Example usage
lst = [1, 2, 3, 4, 5]
n = 2
print(f"List after removing the {n}th element: {remove_nth_element(lst, n)}")
