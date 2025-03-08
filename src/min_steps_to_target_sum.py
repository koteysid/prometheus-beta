from typing import List, Optional

def min_steps_to_target_sum(numbers: List[int], target: int) -> Optional[int]:
    """
    Find the minimum number of steps to reach the target sum using given numbers.
    
    Each number can be used only once, and steps can involve addition or subtraction.
    
    Args:
        numbers (List[int]): List of integers to use for reaching the target
        target (int): The target sum to reach
    
    Returns:
        Optional[int]: Minimum number of steps to reach the target, or None if impossible
    
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    
    Examples:
        >>> min_steps_to_target_sum([1, 2, 3, 4], 7)  # 2 steps: 3 + 4 = 7 
        2
        >>> min_steps_to_target_sum([1, 2, 3, 4], 10)  # None 
        None
    """
    # Edge cases
    if not numbers:
        return None
    
    def backtrack(index: int, current_sum: int) -> Optional[int]:
        # Base cases
        if current_sum == target:
            return 0
        
        # Stop if we've gone through all numbers
        if index >= len(numbers):
            return None
        
        # Try adding the current number
        add_result = backtrack(index + 1, current_sum + numbers[index])
        if add_result is not None:
            add_result += 1
        
        # Try subtracting the current number 
        sub_result = backtrack(index + 1, current_sum - numbers[index])
        if sub_result is not None:
            sub_result += 1
        
        # Return the minimum of valid results
        results = [r for r in [add_result, sub_result] if r is not None]
        return min(results) if results else None
    
    # Try starting from the very beginning
    return backtrack(0, 0)