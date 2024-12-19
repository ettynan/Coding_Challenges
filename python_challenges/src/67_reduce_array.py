'''Given an integer array, reduce the array to a single element - minimized cost'''

import heapq

def minimize_cost(arr):
    if len(arr) < 2:
        return 0  # No cost if the array has one or no elements

    # Create a min-heap from the array
    heapq.heapify(arr)
    total_cost = 0

    while len(arr) > 1:
        # Extract the two smallest elements
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        cost = first + second

        # Add the cost to the total
        total_cost += cost

        # Push the sum back into the heap
        heapq.heappush(arr, cost)

    return total_cost

# Example usage
arr = [4, 3, 2, 6]
print("Minimized Cost:", minimize_cost(arr))
