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
    
    # If numbers and target are empty/zero
    if target == 0:
        if 0 in numbers:
            return 1
        return 0
    
    # Try all possible ways to reach target using addition/subtraction
    for step_count in range(1, len(numbers) + 1):
        for subset in combinations(numbers, step_count):
            # Check all sign combinations for subset
            for signs in range(1 << step_count):
                current_sum = 0
                for i, num in enumerate(subset):
                    # Use bit manipulation to determine sign
                    current_sum += num if signs & (1 << i) else -num
                
                if current_sum == target:
                    return step_count
    
    return None