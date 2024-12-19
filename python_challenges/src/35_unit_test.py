'''Write a simple unit test for a function that adds two numbers'''

import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

# Run the tests
unittest.main(argv=[''], verbosity=2, exit=False)
