'''Create a program to implement a stack using a list'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Adds an item to the stack."""
        self.stack.append(item)

    def pop(self):
        """Removes and returns the top item from the stack."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        """Returns the top item of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Returns the number of items in the stack."""
        return len(self.stack)

# Example usage
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(f"Top item: {my_stack.peek()}")
print(f"Popped item: {my_stack.pop()}")
print(f"Stack size: {my_stack.size()}")
print(f"Is the stack empty? {my_stack.is_empty()}")
