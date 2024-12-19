'''Create a program that checks if a year is a leap year'''

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Example usage
year = 2024
print(f"Year {year} is a leap year: {is_leap_year(year)}")
