'''Write a program to print the multiplication table of a given number'''

def print_multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Example usage
num = 5
print(f"Multiplication table for {num}:")
print_multiplication_table(num)
