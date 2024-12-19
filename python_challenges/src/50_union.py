'''Create a program that finds the intersection and union of two sets'''

def set_operations(set1, set2):
    intersection = set1 & set2
    union = set1 | set2

    print(f"Intersection: {intersection}")
    print(f"Union: {union}")

# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_operations(set1, set2)
