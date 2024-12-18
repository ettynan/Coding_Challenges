def calculate_angle(hour, minute):
    # Ensure the hour is in 12-hour format
    if hour >= 12:
        hour -= 12

    # Calculate the angle of the minute hand
    minute_angle = minute * 6

    # Calculate the angle of the hour hand
    hour_angle = (hour % 12) * 30 + (minute / 60) * 30

    # Calculate the difference between the two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle
    return min(angle, 360 - angle)

# Example usage
print(calculate_angle(3, 15))  # Output: 7.5 degrees
