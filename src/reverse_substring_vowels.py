def reverse_substring_vowels(s: str, start: int, end: int) -> str:
    """
    Reverse the vowels in a specified substring of a given string.
    
    Args:
        s (str): The input string
        start (int): The starting index of the substring (inclusive)
        end (int): The ending index of the substring (exclusive)
    
    Returns:
        str: A new string with vowels in the specified substring reversed
    
    Raises:
        ValueError: If start or end indices are out of bounds
        ValueError: If start is greater than end
    """
    # Validate input indices
    if start < 0 or end > len(s) or start > end:
        raise ValueError("Invalid substring indices")
    
    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Convert string to list for easier manipulation
    chars = list(s)
    
    # Extract vowels from the substring
    substring_vowels = [char for char in chars[start:end] if char in vowels]
    
    # Reverse the extracted vowels
    substring_vowels = substring_vowels[::-1]
    
    # Create a new list to build the result
    result_chars = chars.copy()
    
    # Iterate through the substring and replace vowels
    vowel_index = 0
    for i in range(start, end):
        if chars[i] in vowels:
            result_chars[i] = substring_vowels[vowel_index]
            vowel_index += 1
    
    return ''.join(result_chars)