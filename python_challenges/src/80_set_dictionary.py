'''Program to implement a Set using a Dictionary'''

# Program to implement a Set using a Dictionary

class Set:
    def __init__(self):
        self.elements = {}  # Dictionary to store set elements

    def add(self, element):
        self.elements[element] = True  # Add element to the set (using dictionary key)

    def remove(self, element):
        if element in self.elements:
            del self.elements[element]  # Remove element from the set
        else:
            print(f"Element {element} not found.")

    def contains(self, element):
        return element in self.elements  # Check if element is in the set

    def display(self):
        print(f"Set contains: {list(self.elements.keys())}")  # Display all set elements

# Example usage
s = Set()
s.add(1)
s.add(2)
s.add(3)
s.display()  # Output: Set contains: [1, 2, 3]

s.remove(2)
s.display()  # Output: Set contains: [1, 3]

print(s.contains(1))  # Output: True
print(s.contains(2))  # Output: False
