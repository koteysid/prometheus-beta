import pytest
from src.array_intersection import find_array_intersection

def test_basic_intersection():
    """Test basic intersection of two arrays"""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    assert find_array_intersection(arr1, arr2) == [4, 5]

def test_no_intersection():
    """Test when there are no common elements"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert find_array_intersection(arr1, arr2) == []

def test_full_intersection():
    """Test when all elements are the same"""
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    assert find_array_intersection(arr1, arr2) == [1, 2, 3]

def test_intersection_with_duplicates():
    """Test intersection with duplicate elements"""
    arr1 = [1, 2, 2, 3, 4, 4]
    arr2 = [2, 2, 4, 5, 6]
    assert find_array_intersection(arr1, arr2) == [2, 4]

def test_empty_arrays():
    """Test intersection with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert find_array_intersection(arr1, arr2) == []

def test_invalid_input_types():
    """Test invalid input types raise TypeError"""
    with pytest.raises(TypeError, match="Both inputs must be lists"):
        find_array_intersection("not a list", [1, 2, 3])
    
    with pytest.raises(TypeError, match="Both inputs must be lists"):
        find_array_intersection(123, 456)

def test_invalid_element_types():
    """Test arrays with non-integer elements raise TypeError"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_array_intersection([1, 2, "3"], [3, 4, 5])
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_array_intersection([1, 2, 3], [3, 4, 5.5])