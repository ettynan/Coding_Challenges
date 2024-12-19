'''Create a function that calculates the average of a list of numbers'''

def calculate_average(lst):
    return sum(lst) / len(lst) if lst else 0

# Example usage
numbers = [10, 20, 30, 40, 50]
print(f"Average: {calculate_average(numbers)}")
