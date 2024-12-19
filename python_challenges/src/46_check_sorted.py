'''Write a function to check if a given list is sorted'''

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Example usage
my_list = [1, 2, 3, 4]
print(is_sorted(my_list))  # True

unsorted_list = [1, 3, 2, 4]
print(is_sorted(unsorted_list))  # False
