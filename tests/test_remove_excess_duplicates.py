import pytest
from src.remove_excess_duplicates import remove_excess_duplicates

def test_remove_excess_duplicates():
    # Test basic scenario with duplicates
    assert remove_excess_duplicates("aabbccc") == "aabb"
    
    # Test string with no duplicates
    assert remove_excess_duplicates("abcde") == "abcde"
    
    # Test empty string
    assert remove_excess_duplicates("") == ""
    
    # Test short string
    assert remove_excess_duplicates("ab") == "ab"
    
    # Test more complex scenario
    assert remove_excess_duplicates("aaaaabbbbccccdddeee") == "aabbccddde"
    
    # Test mixed character types
    assert remove_excess_duplicates("112233aabbccddee") == "1233aabbccddee"
    
    # Test with special characters
    assert remove_excess_duplicates("!!@@##$$%%") == "!!@@##$$%%"

def test_remove_excess_duplicates_error_handling():
    # Test non-string input
    with pytest.raises(TypeError):
        remove_excess_duplicates(123)
    
    with pytest.raises(TypeError):
        remove_excess_duplicates(None)
    
    with pytest.raises(TypeError):
        remove_excess_duplicates(["a", "b", "c"])