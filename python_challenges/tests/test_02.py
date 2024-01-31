import math
import pytest
from unittest.mock import patch
from src.two_area_circle import area

def test_area_with_valid_radius():
    with patch("builtins.input", return_value="6"):
        assert math.isclose(area(), 113.097335, abs_tol=1e-6)

def test_area_with_invalid_radius():
    with patch("builtins.input", return_value="invalid"):
        with pytest.raises(ValueError):
            area()

