import pytest
from binary_search import binary_search

def test_found_in_middle():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2

def test_found_at_start():
    arr = [2, 4, 6, 8, 10]
    assert binary_search(arr, 2) == 0

def test_found_at_end():
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, 50) == 4

def test_not_found():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 6) == -1

def test_empty_array():
    arr = []
    assert binary_search(arr, 1) == -1

def test_single_element_found():
    arr = [7]
    assert binary_search(arr, 7) == 0

def test_single_element_not_found():
    arr = [7]
    assert binary_search(arr, 3) == -1

def test_duplicates():
    arr = [1, 2, 2, 2, 3]
    # Should return the index of any occurrence of 2 (could be 1, 2, or 3)
    result = binary_search(arr, 2)
    assert result in [1, 2, 3]

def test_negative_numbers():
    arr = [-10, -5, 0, 5, 10]
    assert binary_search(arr, -5) == 1
    assert binary_search(arr, 0) == 2
    assert binary_search(arr, 10) == 4
    assert binary_search(arr, -11) == -1