'''Create a program that uses a lambda function to square each element of a list'''

def square_elements(lst):
    return list(map(lambda x: x ** 2, lst))

# Example usage
lst = [1, 2, 3, 4, 5]
print(f"Squared elements: {square_elements(lst)}")
