'''Write a program that uses recursion to gnerate all permutations of a list'''

def generate_permutations(lst):
    # Base case: if the list is empty or has one element, return the list itself
    if len(lst) == 0:
        return [[]]
    permutations = []
    for i in range(len(lst)):
        # Take the current element and generate permutations of the remaining elements
        rest = lst[:i] + lst[i+1:]
        for perm in generate_permutations(rest):
            permutations.append([lst[i]] + perm)
    return permutations

# Example usage
my_list = [1, 2, 3]
print(generate_permutations(my_list))

