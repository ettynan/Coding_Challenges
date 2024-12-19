'''Write a function to find the largest common divisor of two numbers using a function'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
print(f"GCD of 36 and 60: {gcd(36, 60)}")
