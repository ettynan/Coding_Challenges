'''Write a test case for a function that checks if a number is prime'''

import unittest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestPrimeFunction(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))

# Run the tests
unittest.main(argv=[''], verbosity=2, exit=False)
