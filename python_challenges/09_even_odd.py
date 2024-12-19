'''Write a program to check if a number is even or odd'''

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
num = 7
print(f"The number {num} is {check_even_odd(num)}.")
