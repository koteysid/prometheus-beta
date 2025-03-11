def remove_string_duplicates(input_string):
    """
    Remove duplicate characters from a given string while preserving the original order.

    Args:
        input_string (str): The input string to remove duplicates from.

    Returns:
        str: A string with duplicate characters removed, maintaining the first occurrence order.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Use sets to track seen characters while preserving order and original case
    seen_lower = set()
    result = []
    
    for char in input_string:
        if char.lower() not in seen_lower:
            seen_lower.add(char.lower())
            result.append(char)
    
    return ''.join(result)