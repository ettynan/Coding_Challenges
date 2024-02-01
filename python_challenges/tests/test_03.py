import pytest
from src.three_count_vowels import count_vowels

def test_count_vowels_with_no_vowels():
    result = count_vowels("rhythm")
    assert result == 0

def test_count_vowels_with_all_vowels():
    result = count_vowels("AEIOUaeiou")
    assert result == 10

def test_count_vowels_mixed_case():
    result = count_vowels("Hello World")
    assert result == 3

def test_count_vowels_empty_string():
    result = count_vowels("")
    assert result == 0

def test_count_vowels_with_numbers():
    result = count_vowels("Python3")
    assert result == 1

def test_count_vowels_with_only_numbers():
    result = count_vowels("647293")
    assert result == 0

if __name__ == "__main__":
    pytest.main()
