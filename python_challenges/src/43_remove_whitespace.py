'''Write a program that removes all whitespaces for a given string'''

def remove_whitespaces(input_string):
    return input_string.replace(" ", "")

# Example usage
my_string = "Hello, how are you?"
print(remove_whitespaces(my_string))
