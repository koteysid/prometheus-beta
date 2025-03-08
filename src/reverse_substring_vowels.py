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
    
    # Extract characters and vowels from the substring
    substring = list(s[start:end])
    
    # Collect vowels from the substring
    substring_vowels = [char for char in substring if char in vowels]
    # Reverse the vowels
    substring_vowels = substring_vowels[::-1]
    
    # Reconstruct the substring with reversed vowels
    vowel_index = 0
    for i in range(len(substring)):
        if substring[i] in vowels:
            substring[i] = substring_vowels[vowel_index]
            vowel_index += 1
    
    # Reconstruct the full string
    result = list(s)
    result[start:end] = substring
    
    return ''.join(result)