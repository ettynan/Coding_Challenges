'''Create a program for a double linked lisk implementation using node class'''

# Class for a node in a doubly linked list
class Node:
    def __init__(self, data):
        self.data = data  # The value of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def add_node(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:
            self.head = new_node  # If the list is empty, set the new node as head
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the last node to the new node
            new_node.prev = current  # Set the previous pointer of new node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")  # Indicate the end of the list

    def display_backward(self):
        current = self.head
        if not current:
            print("None")
            return
        while current.next:  # Traverse to the last node
            current = current.next
        while current:  # Traverse backward
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")  # Indicate the end of the list

    def delete_node(self, data):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        # If the node to be deleted is the head
        if current.data == data:
            self.head = current.next  # Move head to next node
            if self.head:  # If the new head exists, update its previous pointer
                self.head.prev = None
            return

        # Traverse the list to find the node
        while current:
            if current.data == data:
                # Adjust pointers to remove the node
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
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
dll = DoublyLinkedList()
dll.add_node(1)
dll.add_node(2)
dll.add_node(3)
dll.display_forward()  # Output: 1 <-> 2 <-> 3 <-> None

dll.delete_node(2)
dll.display_forward()  # Output: 1 <-> 3 <-> None

dll.display_backward()  # Output: 3 <-> 1 <-> None

print(f"Search 3: {dll.search(3)}")  # Output: True
print(f"Length of list: {dll.length()}")  # Output: 2
