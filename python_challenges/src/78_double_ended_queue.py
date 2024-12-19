'''Create a program to implement a double ended queue using a list'''

class Deque:
    def __init__(self):
        self.deque = []

    def enqueue_front(self, item):
        """Add an item to the front of the deque"""
        self.deque.insert(0, item)

    def enqueue_rear(self, item):
        """Add an item to the rear of the deque"""
        self.deque.append(item)

    def dequeue_front(self):
        """Remove and return an item from the front of the deque"""
        if not self.is_empty():
            return self.deque.pop(0)
        return "Deque is empty"

    def dequeue_rear(self):
        """Remove and return an item from the rear of the deque"""
        if not self.is_empty():
            return self.deque.pop()
        return "Deque is empty"

    def peek_front(self):
        """Return the item at the front without removing it"""
        if not self.is_empty():
            return self.deque[0]
        return "Deque is empty"

    def peek_rear(self):
        """Return the item at the rear without removing it"""
        if not self.is_empty():
            return self.deque[-1]
        return "Deque is empty"

    def is_empty(self):
        """Check if the deque is empty"""
        return len(self.deque) == 0

    def size(self):
        """Return the number of elements in the deque"""
        return len(self.deque)

# Example usage
dq = Deque()
dq.enqueue_rear(1)
dq.enqueue_rear(2)
dq.enqueue_front(0)
print(f"Deque front: {dq.peek_front()}")  # Output: 0
print(f"Deque rear: {dq.peek_rear()}")    # Output: 2
print(f"Dequeue from front: {dq.dequeue_front()}")  # Output: 0
print(f"Dequeue from rear: {dq.dequeue_rear()}")    # Output: 2
print(f"Deque is empty: {dq.is_empty()}")  # Output: False
print(f"Deque size: {dq.size()}")  # Output: 1
