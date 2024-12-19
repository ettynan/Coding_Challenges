'''Create a function that converts a string to an integer and handles ValueError'''

def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return "Invalid input: Not an integer"

# Example usage
input_str = "123"
print(f"Converted integer: {string_to_int(input_str)}")
input_str = "abc"
print(f"Converted integer: {string_to_int(input_str)}")
