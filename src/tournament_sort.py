def tournament_sort(arr):
    """
    Implement the tournament sort algorithm.
    
    Tournament sort is a sorting algorithm that uses a tournament tree (binary heap)
    to efficiently sort an array. It works by repeatedly finding the minimum element
    using a tournament-style elimination process.
    
    Args:
        arr (list): The input list to be sorted in ascending order.
    
    Returns:
        list: A new sorted list with elements in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    working_arr = arr.copy()
    
    def compare_and_eliminate(a, b):
        """
        Compare two elements and return the smaller one.
        
        Args:
            a: First element to compare
            b: Second element to compare
        
        Returns:
            The smaller of the two elements
        """
        return a if a < b else b
    
    # Tournament tree implementation
    def create_tournament_tree(arr):
        """
        Create a tournament tree using a bottom-up approach.
        
        Args:
            arr (list): Input list to create tournament tree from
        
        Returns:
            list: Tournament tree representation
        """
        # Create leaf nodes
        tree = [None] * (2 * len(arr) - 1)
        tree[len(arr) - 1 : 2 * len(arr) - 1] = arr
        
        # Build tournament tree from bottom up
        for i in range(len(arr) - 2, -1, -1):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            
            if right_child < len(tree):
                tree[i] = compare_and_eliminate(
                    tree[left_child], tree[right_child]
                )
            else:
                tree[i] = tree[left_child]
        
        return tree
    
    # Sort by repeatedly finding and removing the minimum
    sorted_result = []
    
    while working_arr:
        # Create tournament tree
        tournament_tree = create_tournament_tree(working_arr)
        
        # Get the minimum element (root of the tournament tree)
        min_element = tournament_tree[0]
        sorted_result.append(min_element)
        
        # Remove the minimum element from the working array
        working_arr.remove(min_element)
    
    return sorted_result