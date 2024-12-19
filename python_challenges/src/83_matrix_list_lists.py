'''Program to implement a Matrix using a List of Lists'''

class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[0] * cols for _ in range(rows)]  # Initialize matrix with zeros

    def set_value(self, row, col, value):
        self.matrix[row][col] = value  # Set the value at the specified row and column

    def get_value(self, row, col):
        return self.matrix[row][col]  # Get the value at the specified row and column

    def display(self):
        for row in self.matrix:
            print(row)  # Display the matrix

# Example usage
m = Matrix(3, 3)  # Create a 3x3 matrix
m.set_value(0, 0, 1)
m.set_value(1, 1, 5)
m.set_value(2, 2, 9)
m.display()  # Output: [1, 0, 0]  [0, 5, 0]  [0, 0, 9]
