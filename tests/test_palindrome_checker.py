import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_case_insensitive_palindromes():
    """Test palindromes with mixed case"""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_non_palindromes():
    """Test strings that are not palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("not a palindrome") == False

def test_punctuation_and_spaces():
    """Test palindromes with punctuation and spaces"""
    assert is_palindrome("race a car") == False
    assert is_palindrome("Do geese see God?") == True

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])