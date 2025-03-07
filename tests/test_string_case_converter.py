import pytest
from src.string_case_converter import to_kebab_case

def test_camel_case_conversion():
    """Test conversion of camel case to kebab case"""
    assert to_kebab_case("helloWorld") == "hello-world"
    assert to_kebab_case("HelloWorld") == "hello-world"
    assert to_kebab_case("camelCaseString") == "camel-case-string"

def test_snake_case_conversion():
    """Test conversion of snake case to kebab case"""
    assert to_kebab_case("hello_world") == "hello-world"
    assert to_kebab_case("snake_case_string") == "snake-case-string"

def test_space_separated_conversion():
    """Test conversion of space-separated strings to kebab case"""
    assert to_kebab_case("Hello World") == "hello-world"
    assert to_kebab_case("Multiple Words Test") == "multiple-words-test"

def test_existing_kebab_case():
    """Test that existing kebab case remains unchanged"""
    assert to_kebab_case("existing-kebab-case") == "existing-kebab-case"

def test_mixed_case_conversion():
    """Test conversion of mixed case strings"""
    assert to_kebab_case("MixedCAMELCase") == "mixed-camel-case"

def test_empty_string():
    """Test conversion of empty string"""
    assert to_kebab_case("") == ""

def test_single_word():
    """Test conversion of a single word"""
    assert to_kebab_case("hello") == "hello"
    assert to_kebab_case("Hello") == "hello"

def test_error_handling():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        to_kebab_case(123)
    with pytest.raises(TypeError):
        to_kebab_case(None)

def test_special_characters():
    """Test handling of strings with special characters"""
    assert to_kebab_case("Hello_World!Test") == "hello-world-test"
    assert to_kebab_case("hello world@test") == "hello-world-test"