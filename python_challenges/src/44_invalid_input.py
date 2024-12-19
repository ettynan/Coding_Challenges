'''Write a program that reads an integer from the user and handles invalid inputs'''

def get_integer_input():
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            print(f"You entered: {user_input}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Example usage
get_integer_input()
