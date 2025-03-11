import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    """Test various valid palindromes with different formatting"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("Madam, I'm Adam") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_single_character():
    """Test single character inputs"""
    assert is_palindrome("a") == True
    assert is_palindrome("Z") == True

def test_numbers_and_mixed_case():
    """Test palindromes with numbers and mixed case"""
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22b2a") == False

def test_error_cases():
    """Test error handling"""
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(None)

def test_whitespace_and_punctuation():
    """Test handling of whitespace and punctuation"""
    assert is_palindrome("   ") == True
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("A man a plan a canal Panama!") == True