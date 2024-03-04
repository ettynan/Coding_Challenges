import pytest
from src.four_sum_elements import sum_list

def test_sum_list_empty_list():
    assert sum_list([]) == 0

def test_sum_list_single_element():
    assert sum_list([5]) == 5

def test_sum_list_multiple_elements():
    assert sum_list([1, 3, 5, 7, 9]) == 25

def test_sum_list_negative_numbers():
    assert sum_list([-1, -3, 5, 7, -9]) == -1

def test_sum_list_mixed_numbers():
    assert sum_list([1.5, 2.5, 3.5]) == 7.5

def test_sum_list_strings():
    with pytest.raises(TypeError):
        sum_list(['a', 'b', 'c'])

if __name__ == '__main__':
    pytest.main()
