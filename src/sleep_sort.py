import threading
import time
from typing import List, Union

def sleep_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Implement the Sleep Sort algorithm with improved synchronization.
    
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
    
    # Find max value to scale sleep time
    max_val = max(arr) if arr else 0
    
    # Thread-safe result list and synchronization primitives
    result = []
    result_lock = threading.Lock()
    all_done = threading.Event()
    
    # Create threads for each element
    threads = []
    for num in arr:
        def worker(x, max_value):
            # Normalize and scale sleep time 
            sleep_time = (x / max_value) * 0.1  # Fixed scaling factor
            time.sleep(sleep_time)
            
            # Thread-safe append to result
            with result_lock:
                result.append(x)
        
        # Create and start thread
        t = threading.Thread(target=worker, args=(num, max_val))
        t.start()
        threads.append(t)
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    return result