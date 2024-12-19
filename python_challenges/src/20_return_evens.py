'''Write a function that takes a list of numbers and returns a new list containing only the even numbers'''

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example usage
numbers = [1, 2, 3, 4, 5, 6]
print(f"Even numbers: {filter_even_numbers(numbers)}")
