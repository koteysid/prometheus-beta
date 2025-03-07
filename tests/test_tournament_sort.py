import pytest
from src.tournament_sort import tournament_sort

def test_tournament_sort_basic():
    """Test basic sorting functionality"""
    assert tournament_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_tournament_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert tournament_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_tournament_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert tournament_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_tournament_sort_empty_list():
    """Test sorting an empty list"""
    assert tournament_sort([]) == []

def test_tournament_sort_single_element():
    """Test sorting a list with a single element"""
    assert tournament_sort([42]) == [42]

def test_tournament_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert tournament_sort([3, 3, 3, 1, 1, 4]) == [1, 1, 3, 3, 3, 4]

def test_tournament_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert tournament_sort([-1, -5, 0, 3, -2]) == [-5, -2, -1, 0, 3]

def test_tournament_sort_invalid_input():
    """Test handling of invalid input"""
    with pytest.raises(TypeError):
        tournament_sort("not a list")
    
    with pytest.raises(TypeError):
        tournament_sort(None)

def test_tournament_sort_with_floats():
    """Test sorting a list with floating-point numbers"""
    assert tournament_sort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_tournament_sort_preserves_original():
    """Test that the original list is not modified"""
    original = [3, 1, 4, 1, 5]
    sorted_list = tournament_sort(original)
    assert original == [3, 1, 4, 1, 5]
    assert sorted_list == [1, 1, 3, 4, 5]