from typing import List, Optional
from itertools import combinations

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
        >>> min_steps_to_target_sum([1, 2, 3, 4], 7)  # 3 + 4 = 7 
        2
        >>> min_steps_to_target_sum([1, 2, 3, 4], 10)  # None 
        None
    """
    # Edge cases
    if not numbers:
        return None
    
    # Try all possible ways to reach target using addition/subtraction
    for step_count in range(len(numbers) + 1):
        for subset in combinations(numbers, step_count):
            # Check positive combination
            if sum(subset) == target:
                return step_count
            
            # Check negative combination
            if sum(num * (-1 if num in subset else 1) for num in numbers) == target:
                return step_count
    
    return None