import pytest
from src.insertion_sort import insertion_sort

def test_insertion_sort_normal_list():
    """Test sorting a normal list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert insertion_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_insertion_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]

def test_insertion_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]

def test_insertion_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert insertion_sort(arr) == []

def test_insertion_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert insertion_sort(arr) == [42]

def test_insertion_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert insertion_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_insertion_sort_with_floating_point():
    """Test sorting a list with floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert insertion_sort(arr) == [0.58, 1.41, 2.23, 2.71, 3.14]

def test_insertion_sort_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        insertion_sort("not a list")

def test_insertion_sort_handles_mixed_types_of_comparables():
    """Test sorting a list with different comparable types"""
    arr = [5, 2, 'b', 'a', 1, 'c']
    assert insertion_sort(arr) == [1, 2, 5, 'a', 'b', 'c']