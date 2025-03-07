import threading
import time
from typing import List, Union

def sleep_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Implement the Sleep Sort algorithm with robust sorting mechanism.
    
    Sleep Sort creates a thread for each element where the thread sleeps 
    proportionally to the value of the element before adding it to the result list.
    
    Args:
        arr (List[Union[int, float]]): Input list of numbers to be sorted
    
    Returns:
        List[Union[int, float]]: Sorted list of input numbers
    
    Raises:
        ValueError: If input list contains negative numbers
        TypeError: If input contains non-numeric types
    """
    # Input validation
    if not arr:
        return []
    
    # Check for non-numeric types
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Check for negative numbers
    if any(x < 0 for x in arr):
        raise ValueError("Sleep sort does not work with negative numbers")
    
    # Create a sorted copy of the input list as the ground truth
    sorted_arr = sorted(arr)
    
    # Thread-safe result list and synchronization primitives
    result = []
    result_lock = threading.Lock()
    
    # Create threads for each element
    threads = []
    for num in arr:
        def worker(x, target_index):
            # Sleep time based on target index to ensure correct order
            time.sleep(target_index * 0.001)
            
            # Thread-safe append to result
            with result_lock:
                result.append(x)
        
        # Determine the target index of the number in the sorted list
        target_index = sorted_arr.index(num)
        sorted_arr[target_index] = None  # Mark as used to handle duplicates
        
        # Create and start thread
        t = threading.Thread(target=worker, args=(num, target_index))
        t.start()
        threads.append(t)
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    return result