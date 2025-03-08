import pytest
from src.fibonacci_generator import generate_fibonacci

def test_fibonacci_base_cases():
    """Test the base cases for Fibonacci number generation."""
    assert generate_fibonacci(1) == 1, "First Fibonacci number should be 1"
    assert generate_fibonacci(2) == 1, "Second Fibonacci number should be 1"

def test_fibonacci_sequence():
    """Test specific Fibonacci numbers in the sequence."""
    # Known Fibonacci numbers for verification
    expected_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, expected in enumerate(expected_sequence, start=1):
        assert generate_fibonacci(i) == expected, f"Incorrect Fibonacci number for n={i}"

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fibonacci(0)
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fibonacci(-1)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci(1.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci("3")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci(None)