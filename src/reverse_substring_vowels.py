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
    
    # Find positions of vowels in the substring
    vowel_positions = [i for i in range(start, end) if chars[i] in vowels]
    
    # If no vowels or insufficient vowels, return original string
    if len(vowel_positions) <= 1:
        return s
    
    # Reverse vowels at these positions
    for i in range(len(vowel_positions) // 2):
        left_pos = vowel_positions[i]
        right_pos = vowel_positions[len(vowel_positions) - 1 - i]
        
        # Swap vowels
        chars[left_pos], chars[right_pos] = chars[right_pos], chars[left_pos]
    
    return ''.join(chars)