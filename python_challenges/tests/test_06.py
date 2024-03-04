import pytest
from src.six_count_char_occur import count_char

class TestCountChar:

    @staticmethod
    @pytest.mark.parametrize("input_str, letter, expected_result", [
        ('Hello World', 'o', 2),
        ('Testing', 'z', 0),
        ('Hello World', 'oo', 0),
    ])
    def test_count_char(input_str, letter, expected_result):
        result = count_char(input_str, letter)
        assert result == expected_result
