import re

def to_kebab_case(input_string: str) -> str:
    """
    Convert a given string to kebab-case.
    
    Kebab case is a string formatting style where words are lowercase 
    and separated by hyphens. This function handles various input formats:
    - Camel Case
    - Snake Case
    - Space-separated words
    - Mixed case strings
    
    Args:
        input_string (str): The input string to convert to kebab case
    
    Returns:
        str: The input string converted to kebab case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_kebab_case("HelloWorld")
        'hello-world'
        >>> to_kebab_case("hello_world")
        'hello-world'
        >>> to_kebab_case("Hello World")
        'hello-world'
        >>> to_kebab_case("hello-world")
        'hello-world'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Use regex to split the string into words
    # This handles multiple cases: camelCase, PascalCase, snake_case, space separated, and mixed scenarios
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+', input_string)
    
    # Convert words to lowercase and remove any non-alphanumeric characters
    clean_words = []
    for word in words:
        # Remove any non-letter characters and convert to lowercase
        clean_word = re.sub(r'[^a-zA-Z]', '', word).lower()
        if clean_word:
            clean_words.append(clean_word)
    
    # Join words with hyphens
    return '-'.join(clean_words)