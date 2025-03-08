import pytest
from src.reverse_substring_vowels import reverse_substring_vowels

def test_basic_substring_vowel_reversal():
    """Test basic vowel reversal in a substring"""
    assert reverse_substring_vowels("hello world", 0, 5) == "hollo werld"
    assert reverse_substring_vowels("python programming", 7, 17) == "python prigrommang"

def test_no_vowels_in_substring():
    """Test when no vowels are present in the substring"""
    assert reverse_substring_vowels("hello world", 6, 11) == "hello world"

def test_all_vowels_in_substring():
    """Test when substring contains only vowels"""
    assert reverse_substring_vowels("aeiou python", 0, 5) == "uoiea python"

def test_mixed_case_vowels():
    """Test handling of both uppercase and lowercase vowels"""
    assert reverse_substring_vowels("AbcdEfghI", 2, 7) == "AbIdgfhE"

def test_full_string_vowel_reversal():
    """Test when substring covers the entire string"""
    assert reverse_substring_vowels("hello", 0, 5) == "oellh"

def test_invalid_indices():
    """Test error handling for invalid indices"""
    with pytest.raises(ValueError):
        reverse_substring_vowels("hello", -1, 5)
    
    with pytest.raises(ValueError):
        reverse_substring_vowels("hello", 0, 6)
    
    with pytest.raises(ValueError):
        reverse_substring_vowels("hello", 3, 2)

def test_empty_string():
    """Test behavior with an empty string"""
    assert reverse_substring_vowels("", 0, 0) == ""

def test_short_substring():
    """Test vowel reversal in a very short substring"""
    assert reverse_substring_vowels("hello", 2, 3) == "hello"
    assert reverse_substring_vowels("aeiou", 1, 2) == "aeiou"