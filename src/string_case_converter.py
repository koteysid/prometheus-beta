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
    
    # Normalize the string: replace underscores and spaces with hyphens
    normalized = input_string.replace('_', ' ').replace('-', ' ')
    
    # Split the string by uppercase letters and whitespace
    words = []
    current_word = normalized[0].lower()
    for char in normalized[1:]:
        if char.isupper():
            # When an uppercase letter is found, start a new word
            words.append(current_word)
            current_word = char.lower()
        elif char.isspace():
            # When a space is found, append current word and reset
            if current_word:
                words.append(current_word)
            current_word = ''
        else:
            # Add lowercase character to current word
            current_word += char.lower()
    
    # Append the last word
    if current_word:
        words.append(current_word)
    
    # Join words with hyphens
    return '-'.join(words)