import pytest
import time
import random
from src.sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting functionality"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)

def test_sleep_sort_empty_list():
    """Test empty list handling"""
    assert sleep_sort([]) == []

def test_sleep_sort_single_element():
    """Test list with single element"""
    input_list = [42]
    result = sleep_sort(input_list)
    assert result == input_list

def test_sleep_sort_floats():
    """Test sorting with floating-point numbers"""
    input_list = [3.14, 1.41, 2.71, 0.58]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)

def test_sleep_sort_error_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError):
        sleep_sort([-1, 2, 3, -4])

def test_sleep_sort_error_non_numeric():
    """Test that non-numeric types raise a TypeError"""
    with pytest.raises(TypeError):
        sleep_sort([1, 2, 'three', 4])

def test_sleep_sort_performance():
    """Verify that sleep sort works with a larger list"""
    # Generate a random list and check if it's sorted
    input_list = [random.randint(1, 100) for _ in range(50)]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)
    
    # Check that the sorting doesn't take too long
    start_time = time.time()
    sleep_sort(input_list)
    end_time = time.time()
    assert end_time - start_time < 1.0  # Should complete within 1 second