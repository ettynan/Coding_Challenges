'''Create a program that imports the math module and uses its fuctions'''

import math

def math_operations():
    number = 25
    square_root = math.sqrt(number)
    pi_value = math.pi
    power_value = math.pow(2, 3)

    print(f"Square root of {number} is {square_root}")
    print(f"Value of pi is {pi_value}")
    print(f"2 raised to the power of 3 is {power_value}")

# Example usage
math_operations()
