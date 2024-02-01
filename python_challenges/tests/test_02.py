import math
from src.two_area_circle import calculate_area

def test_calculate_area():
    """Tests the calculate_area function with a known radius."""
    radius = 5
    expected_area = math.pi * radius * radius
    assert calculate_area(radius) == expected_area