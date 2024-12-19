'''Create a program for a linked lisk implementation using node class'''

class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty linked list

    def add_node(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:
            self.head = new_node  # If list is empty, make new_node the head
        else:
            current = self.head
            while current.next:
                current = current.next  # Traverse until the end
            current.next = new_node  # Link the new node to the end

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Mark the end of the list

    def delete_node(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next  # Move the head to the next node
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # Remove the node
                return
            current = current.next
        print(f"Node with data {data} not found.")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Example usage
ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None

ll.delete_node(2)
ll.display()  # Output: 1 -> 3 -> None

print(f"Search 3: {ll.search(3)}")  # Output: True
print(f"Length of list: {ll.length()}")  # Output: 2
