def insertion_sort(arr):
    """
    Implement the insertion sort algorithm to sort a list in-place.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list or contains incomparable elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Perform insertion sort
    for i in range(1, len(arr)):
        # Store the current element to insert
        key = arr[i]
        
        # Find the correct position to insert the current element
        j = i - 1
        while j >= 0:
            try:
                # Check if we need to swap based on the type of comparison
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                else:
                    break
            except TypeError:
                # If direct comparison fails, use string representation as a fallback
                if str(arr[j]) > str(key):
                    arr[j + 1] = arr[j]
                    j -= 1
                else:
                    break
        
        # Insert the element in its correct position
        arr[j + 1] = key
    
    return arr