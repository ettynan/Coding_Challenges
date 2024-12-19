'''Create a program to implement a priority queue using a dictionary'''

class PriorityQueue:
    def __init__(self):
        # Initialize the priority queue dictionary
        self.queue = {}

    def enqueue(self, item, priority):
        # Add the item to the queue at the given priority level
        if priority in self.queue:
            self.queue[priority].append(item)
        else:
            self.queue[priority] = [item]

    def dequeue(self):
        # Find the highest priority (smallest number)
        if not self.queue:
            return "Queue is empty"
        
        highest_priority = min(self.queue.keys())
        # Pop the item from the highest priority level
        item = self.queue[highest_priority].pop(0)
        
        # If no more items are left at this priority, remove the priority level
        if not self.queue[highest_priority]:
            del self.queue[highest_priority]
        
        return item

    def peek(self):
        # Get the highest priority item without removing it
        if not self.queue:
            return "Queue is empty"
        
        highest_priority = min(self.queue.keys())
        return self.queue[highest_priority][0]

    def is_empty(self):
        # Check if the priority queue is empty
        return len(self.queue) == 0

# Example usage
pq = PriorityQueue()
pq.enqueue("task1", 3)
pq.enqueue("task2", 1)
pq.enqueue("task3", 2)

print("Dequeuing highest priority task:", pq.dequeue())  # task2 (priority 1)
print("Next highest priority task:", pq.peek())  # task3 (priority 2)
print("Dequeuing next task:", pq.dequeue())  # task3 (priority 2)
print("Dequeuing last task:", pq.dequeue())  # task1 (priority 3)
print("Is queue empty?", pq.is_empty())  # True
