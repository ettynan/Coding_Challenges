'''Create a program to implement a queue using a list'''

class Queue:
    def __init__(self, max_size=None):
        self.queue = []
        self.front = 0  # Pointer to front of the queue
        self.rear = 0  # Pointer to the end of the queue
        self.max_size = max_size

    def enqueue(self, item):
        if self.max_size and self.size() == self.max_size:
            return "Queue is full"
        self.queue.append(item)
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        item = self.queue[self.front]
        self.front += 1
        return item

    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]
        return "Queue is empty"

    def is_empty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

# Example usage
q = Queue(max_size=3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.enqueue(4))  # Output: Queue is full
print(q.dequeue())  # Output: 1
print(q.peek())  # Output: 2
