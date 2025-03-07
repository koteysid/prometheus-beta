import pytest
from src.alternating_path_case import to_alternating_path_case

def test_basic_conversion():
    """Test basic string conversion"""
    assert to_alternating_path_case("hello world") == "hello-WORLD"
    assert to_alternating_path_case("python programming") == "python-PROGRAMMING"

def test_single_word():
    """Test single word input"""
    assert to_alternating_path_case("hello") == "hello"

def test_empty_string():
    """Test empty string input"""
    assert to_alternating_path_case("") == ""

def test_multiple_words():
    """Test multiple words"""
    assert to_alternating_path_case("one two three four") == "one-TWO-THREE-FOUR"

def test_error_handling():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        to_alternating_path_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_path_case(None)

def test_whitespace_handling():
    """Test handling of extra whitespace"""
    assert to_alternating_path_case("  hello   world  ") == "hello-WORLD"