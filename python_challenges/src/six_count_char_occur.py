'''Write a program to count the occurrences of a specific character in a string'''

def get_input():
    input_str = input("Type a string: ")
    letter = input("Pick a single character to get count: ")
    if len(letter) > 1:
        print("Invalid string or too many letters inputed")
        return None, None
    return input_str, letter

def count_char(input_str, letter):
    count = 0
    for char in input_str:
        if char == letter:
            count += 1
    return count

input_str, letter = get_input()
if input_str is not None and letter is not None:
    result = count_char(input_str, letter)
    print("The number of times", letter, "appears in -", input_str, "- is:", result)