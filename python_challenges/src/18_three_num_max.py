'''Create a program to find the largest amongst three numbers'''

def largest_of_three(a, b, c):
    return max(a, b, c)

# Example usage
a, b, c = 10, 20, 15
print(f"The largest number is: {largest_of_three(a, b, c)}")
