'''Write a program that uses a try-except block to handle division by zero'''

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# Example usage
divide_numbers(10, 2)
divide_numbers(10, 0)
