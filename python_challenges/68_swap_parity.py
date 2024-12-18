'''Given a number num, two adjacent digits can be swapped if their parity is the same, that is, both are odd or both are even.'''

def largest_by_parity_swap(num):
    # Convert number to list of digits
    digits = [int(d) for d in str(num)]

    # Separate and sort odd and even digits
    odd_digits = sorted((d for d in digits if d % 2 == 1), reverse=True)
    even_digits = sorted((d for d in digits if d % 2 == 0), reverse=True)

    # Reconstruct the largest number
    result = []
    for d in digits:
        if d % 2 == 1:  # Odd digit
            result.append(odd_digits.pop(0))
        else:  # Even digit
            result.append(even_digits.pop(0))

    return int("".join(map(str, result)))

# Example usage
num = 247531
print("Largest Number by Parity Swap:", largest_by_parity_swap(num))
