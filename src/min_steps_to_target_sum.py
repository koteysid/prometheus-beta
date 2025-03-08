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
        >>> min_steps_to_target_sum([1, 2, 3, 4], 7)  # 3 + 4 = 7 
        2
        >>> min_steps_to_target_sum([1, 2, 3, 4], 10)  # None 
        None
    """
    # Early exits and special cases
    if not numbers:
        return None
    
    # Precompute useful information
    total_sum = sum(abs(num) for num in numbers)
    if target == 0:
        return 1 if 0 in numbers else 0
    
    if target > total_sum or target < -total_sum:
        return None
    
    def dfs(index: int, current_sum: int, steps: int, used: int) -> Optional[int]:
        # Reached target
        if current_sum == target:
            return steps
        
        # Gone past all numbers
        if index >= len(numbers):
            return None
        
        # Avoid using the same number multiple times
        if used & (1 << index):
            return dfs(index + 1, current_sum, steps, used)
        
        # Try adding current number
        add_result = dfs(
            index + 1, 
            current_sum + numbers[index], 
            steps + 1, 
            used | (1 << index)
        )
        
        # Try subtracting current number
        sub_result = dfs(
            index + 1, 
            current_sum - numbers[index], 
            steps + 1, 
            used | (1 << index)
        )
        
        # Results list
        results = [r for r in [add_result, sub_result] if r is not None]
        
        return min(results) if results else None
    
    return dfs(0, 0, 0, 0)