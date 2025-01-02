'''Write an algorithm which finds out the elements which are largest in a row and smallest in a column in a matrix.'''

def find_row_largest_col_smallest(matrix):
    """
    Finds elements in the matrix that are largest in their row and smallest in their column.

    :param matrix: List of lists representing the matrix
    :return: List of elements satisfying the condition
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        # Identify the largest element in the row and its column index
        row_max = max(matrix[i])
        col_indices = [j for j in range(cols) if matrix[i][j] == row_max]

        # Check if this row_max is the smallest in its column(s)
        for col_index in col_indices:
            is_col_min = all(row_max <= matrix[k][col_index] for k in range(rows))
            if is_col_min:
                result.append(row_max)

    return result

# Example usage
matrix = [
    [10, 9, 8],
    [11, 12, 13],
    [12, 13, 14]
]
print("Elements largest in row and smallest in column:", find_row_largest_col_smallest(matrix))

