import pytest
from unittest.mock import patch
from src.six_count_char_occur import get_input, count_char

@pytest.mark.parametrize("user_input, expected_result", [
    (('Hello World', 'o'), 2),
    (('Testing', 'z'), 0),
    (('Hello World', 'oo'), (None, None)),
])
def test_count_char(user_input, expected_result):
    with patch('builtins.input', side_effect=user_input):
        input_str, letter = get_input()
        if expected_result == (None, None):
            assert input_str is None
            assert letter is None
        else:
            result = count_char(input_str, letter)
            assert result == expected_result

if __name__ == '__main__':
    pytest.main()
