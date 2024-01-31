import math

def calculate_area(radius):
    """Calculates the area of a circle given its radius."""
    area = math.pi * pow(radius, 2)
    return area

def get_user_input():
    """Prompts the user for a radius and handles potential input errors using a while loop."""
    while True:
        radius_str = input("Enter the radius: ")
        try:
            radius = float(radius_str)
            return radius
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    radius = get_user_input()
    area = calculate_area(radius)
    print(area)