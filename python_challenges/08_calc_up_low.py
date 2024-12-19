'''Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it'''

def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

# Example usage
s = "Hello World"
upper, lower = count_case(s)
print(f"Uppercase: {upper}, Lowercase: {lower}")
