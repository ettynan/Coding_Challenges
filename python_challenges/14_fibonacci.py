'''Write a program to write the first n numbers of the Fibonacci sequence'''

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example usage
n = 10
print(f"The first {n} Fibonacci numbers: {fibonacci(n)}")
