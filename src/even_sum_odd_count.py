def analyze_number_list(numbers):
    """
    Analyze a list of numbers to calculate the sum of even numbers and count of odd numbers.

    Args:
        numbers (list): A list of integers to analyze.

    Returns:
        tuple: A tuple containing two elements:
            - The sum of all even numbers in the list
            - The count of odd numbers in the list

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Calculate sum of positive even numbers and count of odd numbers
    even_sum = sum(num for num in numbers if num % 2 == 0 and num > 0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    
    return even_sum, odd_count