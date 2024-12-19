'''Create a program that generates a random number between a given range'''

import random

def generate_random_number(start, end):
    return random.randint(start, end)

# Example usage
start = 1
end = 100
print(f"Random number between {start} and {end}: {generate_random_number(start, end)}")
