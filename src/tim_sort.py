def insertion_sort(arr, left, right):
    """
    Perform insertion sort on a small portion of the array.
    
    Args:
        arr (list): The list to be sorted
        left (int): Starting index of the portion to sort
        right (int): Ending index of the portion to sort
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays of the given array.
    
    Args:
        arr (list): The list containing subarrays to merge
        left (int): Starting index of the first subarray
        mid (int): Ending index of the first subarray
        right (int): Ending index of the second subarray
    """
    # Create temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0  # Indices for left and right subarrays
    k = left  # Index for merged array
    
    # Merge elements comparing from both subarrays
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left_arr if any
    while i < len(left_arr):
        arr[k] = left_arr[i]
        k += 1
        i += 1
    
    # Copy remaining elements of right_arr if any
    while j < len(right_arr):
        arr[k] = right_arr[j]
        k += 1
        j += 1
    
    return arr

def tim_sort(arr):
    """
    Implement Tim sort algorithm.
    
    Tim sort is a hybrid sorting algorithm that combines merge sort and insertion sort.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: Sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty or single element list is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a small run size (typically between 32 and 64)
    MIN_RUN = 32
    
    # Sort small runs using insertion sort
    n = len(arr)
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)
    
    # Merge sorted runs
    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min(start + size * 2 - 1, n - 1)
            
            # Only merge if there are at least two runs
            if mid < end:
                merge(arr, start, mid, end)
        
        size *= 2
    
    return arr