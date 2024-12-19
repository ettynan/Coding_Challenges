'''Create a program to remov a specific lement from a set.'''

def remove_element_from_set(my_set, element):
    if element in my_set:
        my_set.remove(element)
    return my_set

# Example usage
my_set = {1, 2, 3, 4, 5}
element = 3
print(f"Set after removing {element}: {remove_element_from_set(my_set, element)}")
