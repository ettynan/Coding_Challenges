'''Program to implement a Graph using a Dictionary of Lists'''

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to represent the graph

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []  # Initialize an empty list for the node

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append(node2)  # Add node2 as an adjacent node of node1
        self.graph[node2].append(node1)  # Add node1 as an adjacent node of node2 (for undirected graph)

    def display(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")  # Display each node and its adjacent nodes

# Example usage
g = Graph()
g.add_node(1)
g.add_node(2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.display()  # Output: 1: [2, 3]  2: [1]  3: [1]
