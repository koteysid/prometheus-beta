import pytest
from src.tim_sort import tim_sort

def test_tim_sort_empty_list():
    """Test sorting an empty list"""
    assert tim_sort([]) == []

def test_tim_sort_single_element():
    """Test sorting a list with a single element"""
    assert tim_sort([42]) == [42]

def test_tim_sort_sorted_list():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert tim_sort(arr) == [1, 2, 3, 4, 5]

def test_tim_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert tim_sort(arr) == [1, 2, 3, 4, 5]

def test_tim_sort_random_list():
    """Test sorting a random list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert tim_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_tim_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert tim_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_tim_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 10, -3, 0, 7, -1]
    assert tim_sort(arr) == [-5, -3, -1, 0, 7, 10]

def test_tim_sort_floating_point():
    """Test sorting a list of floating point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert tim_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_tim_sort_large_list():
    """Test sorting a larger list of integers"""
    arr = list(range(100, 0, -1))
    assert tim_sort(arr) == list(range(1, 101))

def test_tim_sort_invalid_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        tim_sort("not a list")
        tim_sort(123)
        tim_sort(None)