import pytest
from first import calculate_average

def test_average_of_positive_numbers():
    assert calculate_average([1, 2, 3, 4, 5]) == 3

def test_average_of_negative_numbers():
    assert calculate_average([-1, -2, -3]) == -2

def test_average_of_mixed_numbers():
    assert calculate_average([1, -1, 1, -1]) == 0

def test_average_of_empty_list():
    assert calculate_average([]) == 0

def test_average_is_not_negative_for_positive_input():
    result = calculate_average([10, 20, 30])
    assert result >= 0, "Average should not be negative for positive numbers"