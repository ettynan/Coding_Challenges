'''Create a function that checks if a number is a perfect square'''

import math

def is_perfect_square(num):
    return num == math.isqrt(num) ** 2

# Example usage
number = 16
print(f"Is {number} a perfect square? {is_perfect_square(number)}")
number = 15
print(f"Is {number} a perfect square? {is_perfect_square(number)}")
