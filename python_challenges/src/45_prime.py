'''Write a function to check if a number if a prime number'''

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
print(is_prime(11))  # True
print(is_prime(10))  # False
