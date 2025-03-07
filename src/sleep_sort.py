import threading
import time
from typing import List, Union

def sleep_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Implement the Sleep Sort algorithm.
    
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
    
    # Thread-safe result list and synchronization primitive
    result = []
    result_lock = threading.Lock()
    
    # Create threads for each element
    threads = []
    for num in arr:
        def worker(x):
            # Sleep proportional to the value 
            time.sleep(x * 0.01)  # Scaled sleep time
            
            # Thread-safe append to result
            with result_lock:
                result.append(x)
        
        # Create and start thread
        t = threading.Thread(target=worker, args=(num,))
        t.start()
        threads.append(t)
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    return result