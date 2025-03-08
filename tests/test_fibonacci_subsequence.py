import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_fibonacci_subsequence_basic():
    """Test basic Fibonacci subsequence generation."""
    assert generate_fibonacci_subsequence(5) == [0, 1, 1, 2, 3]

def test_fibonacci_subsequence_zero_length():
    """Test generating a subsequence of length 0."""
    assert generate_fibonacci_subsequence(0) == []

def test_fibonacci_subsequence_single_element():
    """Test generating a subsequence of length 1."""
    assert generate_fibonacci_subsequence(1) == [0]

def test_fibonacci_subsequence_two_elements():
    """Test generating a subsequence of length 2."""
    assert generate_fibonacci_subsequence(2) == [0, 1]

def test_fibonacci_subsequence_longer():
    """Test generating a longer Fibonacci subsequence."""
    assert generate_fibonacci_subsequence(8) == [0, 1, 1, 2, 3, 5, 8, 13]

def test_fibonacci_subsequence_invalid_input_negative():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Length of subsequence must be non-negative"):
        generate_fibonacci_subsequence(-1)

def test_fibonacci_subsequence_invalid_input_type():
    """Test that an invalid input type raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_subsequence("3")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_subsequence(3.5)