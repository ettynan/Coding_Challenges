'''Create a program to calculate the area of a circle given its radius'''
import math

def area():
    radius = float(input("Give the radius: "))
    area = math.pi * pow(radius, 2)
    return area

print(area())