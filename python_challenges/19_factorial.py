'''Write a function to calculate the factorial of a number.'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
n = 5
print(f"The factorial of {n} is: {factorial(n)}")
