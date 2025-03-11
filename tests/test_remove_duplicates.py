import pytest
from src.remove_duplicates import remove_string_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal."""
    assert remove_string_duplicates("hello") == "helo"

def test_remove_duplicates_all_unique():
    """Test string with all unique characters."""
    assert remove_string_duplicates("abcdef") == "abcdef"

def test_remove_duplicates_empty_string():
    """Test empty string."""
    assert remove_string_duplicates("") == ""

def test_remove_duplicates_mixed_case():
    """Test mixed case characters."""
    assert remove_string_duplicates("HeLLo") == "Helo"

def test_remove_duplicates_with_spaces():
    """Test duplicate removal with spaces."""
    assert remove_string_duplicates("hello world") == "helo wrd"

def test_remove_duplicates_with_numbers():
    """Test duplicate removal with numbers."""
    assert remove_string_duplicates("112233") == "123"

def test_remove_duplicates_invalid_input():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_string_duplicates(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_string_duplicates(None)