import pytest
from src.even_sum_odd_count import analyze_number_list

def test_mixed_numbers():
    """Test with a list of mixed even and odd numbers."""
    result = analyze_number_list([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)

def test_only_even_numbers():
    """Test with a list of only even numbers."""
    result = analyze_number_list([2, 4, 6, 8])
    assert result == (20, 0)

def test_only_odd_numbers():
    """Test with a list of only odd numbers."""
    result = analyze_number_list([1, 3, 5, 7])
    assert result == (0, 4)

def test_empty_list():
    """Test with an empty list."""
    result = analyze_number_list([])
    assert result == (0, 0)

def test_negative_numbers():
    """Test with a list containing negative and positive numbers."""
    result = analyze_number_list([-1, -2, -3, -4, 5, 6])
    result = analyze_number_list([-1, -2, -3, -4, 5, 6])
    assert result == (2, 3)

def test_invalid_input_non_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        analyze_number_list(123)

def test_invalid_input_non_integers():
    """Test that a TypeError is raised for list with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        analyze_number_list([1, 2, '3', 4])