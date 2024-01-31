'''Create a program to calculate the area of a circle given its radius'''
import math

def area():
    '''Gains user inputted radius and calculates a circle's area'''
    try:
        radius = float(input("Enter the radius: "))
    except EOFError:
        # Handle EOFError:
        print("Error: Unexpected end of input. Please provide valid input.")
        # Optionally, ask the user for input again or take appropriate action
        radius = float(input("Enter the radius again: "))
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        radius = float(input("Enter the radius again: "))
    area = math.pi * pow(radius, 2)
    return area

print(area())