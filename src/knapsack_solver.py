def solve_knapsack(weights, values, capacity):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        weights (list): List of item weights
        values (list): List of item values
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        tuple: A tuple containing (maximum value, selected items)
    
    Raises:
        ValueError: If input lists have different lengths or invalid inputs
    """
    # Input validation
    if not (weights and values and len(weights) == len(values)):
        raise ValueError("Weights and values lists must be non-empty and of equal length")
    
    if capacity < 0:
        raise ValueError("Knapsack capacity must be non-negative")
    
    n = len(weights)
    
    # Initialize dynamic programming table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build the dynamic programming table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If current item can't be included due to weight
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Maximum of including or excluding current item
                dp[i][w] = max(
                    dp[i-1][w],  # Exclude current item
                    dp[i-1][w - weights[i-1]] + values[i-1]  # Include current item
                )
    
    # Trace back to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    # Reverse to maintain original order and return max value with selected items
    return dp[n][capacity], list(reversed(selected_items))