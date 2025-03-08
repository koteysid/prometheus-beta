def remove_excess_duplicates(input_string):
    """
    Remove characters that appear more than twice in the given string.
    
    Args:
        input_string (str): The input string to process
    
    Returns:
        str: A string with characters appearing more than twice removed
    
    Raises:
        TypeError: If input is not a string
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty or too short to have duplicates, return as-is
    if len(input_string) <= 2:
        return input_string
    
    # Count character occurrences
    char_counts = {}
    result = []
    
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
        
        # Keep the character only if it appears twice or less
        if char_counts[char] <= 2:
            result.append(char)
    
    return ''.join(result)