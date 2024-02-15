import pytest
from src.five_max_min_val import min_val, max_val

def test_min_val():
    assert min_val([10, 28, 3, 4, 5]) == 3

def test_max_val():
    assert max_val([10, 28, 3, 4, 5]) == 28

def test_min_val_empty_list():
    with pytest.raises(ValueError):
        min_val([])

def test_max_val_empty_list():
    with pytest.raises(ValueError):
        max_val([])

def test_min_val_duplicate_values():
    assert min_val([10, 10, 3, 4, 5]) == 3

def test_max_val_duplicate_values():
    assert max_val([10, 10, 3, 4, 5]) == 10

if __name__ == "__main__":
    pytest.main()